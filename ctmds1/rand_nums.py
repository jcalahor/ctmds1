import typer
import numpy as np
import logging
from typing import Dict
from datetime import datetime, timedelta
import pytz
from constants import Countries, CountryDefaultPriceBase, GranularityParam, Commodity
from curves import SEASON_CURVE_BY_COUNTRY_COMMODITY, HOURLY_CURVE_BY_COUNTRY_COMMODITY


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

app = typer.Typer()


def numpy_method(n: int):
    random_numbers = np.random.uniform(1, 100, size=n)
    return random_numbers


@app.command()
def country_date(
    commodity: Commodity = Commodity.crude,
    for_date: str = typer.Option(...),
    country: Countries = Countries.GB,
    granularity: GranularityParam = GranularityParam.h,
):
    n, quarter = get_calendar_details(for_date, "America/New_York")

    def rand_numbers(n: int, base):
        low_limit = base - 10
        upper_limit = base + 10
        random_numbers = np.random.uniform(low_limit, upper_limit, size=n)
        return random_numbers

    def get_prices_h(n):
        numbers = rand_numbers(n, CountryDefaultPriceBase[country])
        result_dict: Dict[str, float] = {}
        minute = 0
        for i in range(n):
            hour = i
            time_str = f"{hour:02}{minute:02}"
            result_dict[time_str] = round(
                float(numbers[i])
                * HOURLY_CURVE_BY_COUNTRY_COMMODITY[(country, commodity)][hour]
                * SEASON_CURVE_BY_COUNTRY_COMMODITY[(country, commodity)][quarter],
                2,
            )
        return result_dict

    def get_prices_hh(n):
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
                * HOURLY_CURVE_BY_COUNTRY_COMMODITY[(country, commodity)][hour]
                * SEASON_CURVE_BY_COUNTRY_COMMODITY[(country, commodity)][quarter],
                2,
            )
        return result_dict

    STRATEGIES = {GranularityParam.h: get_prices_h, GranularityParam.hh: get_prices_hh}

    prices = STRATEGIES[granularity](n)
    print(prices)
    return prices


if __name__ == "__main__":
    app()
