import typer
from typing import Dict

from datetime import datetime, timedelta
import pytz
import numpy as np
import logging
import os
import yaml


from contextlib import asynccontextmanager


from ctmds1.power_setup import factor_cost_by_country

from ctmds1.constants import (
    Countries,
    CountryDefaultPriceBase,
    GranularityParam,
    Commodity,
)

from fastapi import FastAPI
from ctmds1.repository import (
    init_db,
    get_hourly_curve_factor,
    get_season_curve_factor,
    get_currency_factor,
    get_prices,
    store_price,
)


config_path = "ctmds1/config.yaml"

if os.path.exists(config_path):
    with open(config_path, "r") as f:
        config = yaml.safe_load(f)
        logging.config.dictConfig(config)


# Use the root logger to capture everything
logger = logging.getLogger()


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.db = await init_db()

    logger.info("Database initialized and ready.")

    yield

    # On shutdown: Clean up resources (close the connection)
    app.state.db.close()
    logger.info("Database connection closed.")


app = FastAPI(lifespan=lifespan)


def get_calendar_details(date_str, timezone_str):
    tz = pytz.timezone(timezone_str)
    date = datetime.strptime(date_str, "%Y-%m-%d").date()

    start = tz.localize(datetime.combine(date, datetime.min.time()), is_dst=None)

    next_day = date + timedelta(days=1)
    end = tz.localize(datetime.combine(next_day, datetime.min.time()), is_dst=None)

    hours = (end - start).total_seconds() / 3600

    quarter = "Q1"
    if date.month in (1, 2, 3):
        quarter = "Q1"
    elif date.month in (4, 5, 6):
        quarter = "Q2"
    elif date.month in (7, 8, 9):
        quarter = "Q3"
    else:
        quarter = "Q4"

    return int(hours), quarter


@app.get("/country-date/{commodity}/{for_date}/{country}/{granularity}")
def country_date(
    commodity: Commodity = Commodity.crude,
    for_date: str = typer.Option(...),
    country: Countries = Countries.GB,
    granularity: GranularityParam = GranularityParam.h,
):
    n, quarter = get_calendar_details(for_date, "America/New_York")
    db = app.state.db

    def rand_numbers(n: int, base):
        low_limit = base - 1
        upper_limit = base + 1
        random_numbers = np.random.uniform(low_limit, upper_limit, size=n)
        return random_numbers

    def lookup_prices(n):
        logger.info("Call lookup_prices")
        raw_prices = get_prices(db, country, commodity, for_date)
        if not raw_prices:
            logger.info("Generating prices")
            raw_prices = []
            hourly_factors = get_hourly_curve_factor(db, country, commodity)
            season_factors = get_season_curve_factor(db, country, commodity)
            currency_factor = get_currency_factor(db, country)
            n = n * 2
            numbers = rand_numbers(n, CountryDefaultPriceBase[(country, commodity)])
            minute = 0
            for i in range(n):
                hour = i // 2
                minute = 30 * (i % 2)
                price = round(
                    float(numbers[i])
                    * hourly_factors[hour]
                    * season_factors[quarter]
                    * currency_factor
                    * factor_cost_by_country(commodity, hour, country),
                    2,
                )
                raw_price = {"hour": hour, "minute": minute, "price": price}
                raw_prices.append(raw_price)
                store_price(db, country, commodity, for_date, hour, minute, price)
        else:
            logger.info("Loaded stored prices")

        included_minute_range = [0] if granularity == GranularityParam.h else [0, 30]
        result_prices: Dict[str, float] = {}
        for raw_price_entry in raw_prices:
            minute = raw_price_entry["minute"]
            if minute in included_minute_range:
                hour = raw_price_entry["hour"]
                price = raw_price_entry["price"]
                time_str = f"{hour:02}{minute:02}"
                result_prices[time_str] = price
        return result_prices

    prices = lookup_prices(n)
    return {"prices": prices}


@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI with Poetry!"}
