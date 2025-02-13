import typer
import numpy as np
import time
import logging
from typing import Dict

# Configure the logger
logging.basicConfig(
    level=logging.DEBUG,  # Set the logging level
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",  # Log message format
    datefmt="%Y-%m-%d %H:%M:%S"  # Date format
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
def country_date(for_date: str = typer.Option(...), country_code: str = typer.Option(...), granularity: str = typer.Option(...)):
    def rand_numbers(n: int, base):
        low_limit = base - 10
        upper_limit = base + 10
        random_numbers = np.random.uniform(low_limit, upper_limit, size=n)
        return random_numbers
    
    if country_code not in COUNTRIES:
        print ("Country not supported")
        
    n = 24
    if granularity == "hh":
        n = n * 2
        
    numbers = rand_numbers(n, COUNTRIES[country_code])
    result_dict: Dict[str, float] = {}
    
    if granularity == "hh":
        for i in range(n):
            hour = i // 2           
            minute = 30 * (i % 2)                        
            time_str = f"{hour:02}{minute:02}"
            result_dict[time_str] = float(numbers[i])
    else:
        minute = 0
        for i in range(n):
            hour = i            
            time_str = f"{hour:02}{minute:02}"
            result_dict[time_str] = float(numbers[i])
        
    print (result_dict)



@app.command()
def generate(number: int = typer.Option(..., help="Number of random numbers to generate")):
    """Generate X number of random numbers"""

    start_time = time.perf_counter()
    logger.info(f"Current time: {start_time} seconds")
    numpy_method(number)
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    logger.info(f"Elapsed time: {elapsed_time} seconds")


if __name__ == "__main__":
    app()
