import typer
import numpy as np
import time
import logging
from typing import Dict
from enum import Enum
from datetime import datetime, timedelta
import pytz
from constants import Countries


def get_hours_in_day(date_str, timezone_str):
    tz = pytz.timezone(timezone_str)
    date = datetime.strptime(date_str, "%Y-%m-%d").date()

    start = tz.localize(datetime.combine(date, datetime.min.time()), is_dst=None)

    next_day = date + timedelta(days=1)
    end = tz.localize(datetime.combine(next_day, datetime.min.time()), is_dst=None)

    hours = (end - start).total_seconds() / 3600
    return int(hours)


class GranularityParam(str, Enum):
    h = "h"
    hh = "hh"


# Configure the logger
logging.basicConfig(
    level=logging.DEBUG,  # Set the logging level
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",  # Log message format
    datefmt="%Y-%m-%d %H:%M:%S",  # Date format
)
logger = logging.getLogger(__name__)

app = typer.Typer()

COUNTRIES = {
    "GB": 61,
    "FR": 58,
    "NL": 52,
    "DE": 57,
}


def numpy_method(n: int):
    random_numbers = np.random.uniform(1, 100, size=n)
    return random_numbers


@app.command()
def country_date(
    for_date: str = typer.Option(...),
    country_code: str = typer.Option(...),
    granularity: GranularityParam = GranularityParam.h,
):
    def rand_numbers(n: int, base):
        low_limit = base - 10
        upper_limit = base + 10
        random_numbers = np.random.uniform(low_limit, upper_limit, size=n)
        return random_numbers

    def get_prices_h(country_code, n):
        numbers = rand_numbers(n, COUNTRIES[country_code])
        result_dict: Dict[str, float] = {}
        minute = 0
        for i in range(n):
            hour = i
            time_str = f"{hour:02}{minute:02}"
            result_dict[time_str] = float(numbers[i])
        return result_dict

    def get_prices_hh(country_code, n):
        n = n * 2
        numbers = rand_numbers(n, COUNTRIES[country_code])
        result_dict: Dict[str, float] = {}
        minute = 0
        for i in range(n):
            hour = i // 2
            minute = 30 * (i % 2)
            time_str = f"{hour:02}{minute:02}"
            result_dict[time_str] = float(numbers[i])
        return result_dict

    STRATEGIES = {GranularityParam.h: get_prices_h, GranularityParam.hh: get_prices_hh}

    if country_code not in COUNTRIES:
        print("Country not supported")

    n = get_hours_in_day(for_date, "America/New_York")
    print(n)
    result_dict = STRATEGIES[granularity](country_code, n)
    print(result_dict)


@app.command()
def generate(
    number: int = typer.Option(..., help="Number of random numbers to generate")
):
    """Generate X number of random numbers"""

    start_time = time.perf_counter()
    logger.info(f"Current time: {start_time} seconds")
    numpy_method(number)
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    logger.info(f"Elapsed time: {elapsed_time} seconds")


if __name__ == "__main__":
    app()
