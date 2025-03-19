import typer
import numpy as np
import logging
from typing import Dict
from datetime import datetime, timedelta
import pytz
from contextlib import asynccontextmanager
from power_setup import factor_cost_by_country

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
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.db = await init_db()

    print("Database initialized and ready.")

    yield

    # On shutdown: Clean up resources (close the connection)
    app.state.db.close()
    print("Database connection closed.")


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


# Configure the logger
logging.basicConfig(
    level=logging.DEBUG,  # Set the logging level
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",  # Log message format
    datefmt="%Y-%m-%d %H:%M:%S",  # Date format
)
logger = logging.getLogger(__name__)


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
        low_limit = base - 10
        upper_limit = base + 10
        random_numbers = np.random.uniform(low_limit, upper_limit, size=n)
        return random_numbers

    def get_prices_h(n):
        hourly_factors = get_hourly_curve_factor(db, country, commodity)
        season_factors = get_season_curve_factor(db, country, commodity)
        currency_factor = get_currency_factor(db, country)
        print(hourly_factors)
        numbers = rand_numbers(n, CountryDefaultPriceBase[country])
        result_dict: Dict[str, float] = {}
        minute = 0
        for i in range(n):
            hour = i
            time_str = f"{hour:02}{minute:02}"
            result_dict[time_str] = round(
                float(numbers[i])
                * hourly_factors[hour]
                * season_factors[quarter]
                * currency_factor
                * factor_cost_by_country(commodity, hour, country),
                2,
            )
        return result_dict

    def get_prices_hh(n):
        hourly_factors = get_hourly_curve_factor(db, country, commodity)
        season_factors = get_season_curve_factor(db, country, commodity)
        currency_factor = get_currency_factor(db, country)
        print(hourly_factors)
        n = n * 2
        numbers = rand_numbers(n, CountryDefaultPriceBase[country])
        result_dict: Dict[str, float] = {}
        minute = 0
        for i in range(n):
            hour = i // 2
            minute = 30 * (i % 2)
            time_str = f"{hour:02}{minute:02}"
            result_dict[time_str] = round(
                float(numbers[i])
                * hourly_factors[hour]
                * season_factors[quarter]
                * currency_factor,
                *factor_cost_by_country(commodity, hour, country),
                2,
            )
        return result_dict

    STRATEGIES = {GranularityParam.h: get_prices_h, GranularityParam.hh: get_prices_hh}

    prices = STRATEGIES[granularity](n)
    return {"prices": prices}


@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI with Poetry!"}
