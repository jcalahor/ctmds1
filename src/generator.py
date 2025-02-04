import typer
import numpy as np
import time
import random

app = typer.Typer()


def numpy_method(number: int):
    random_numbers = np.random.uniform(1, 100, size=number)
    print(len(random_numbers))
    return random_numbers


def iterative_method(number: int):
    random_numbers = [random.uniform(1, 100) for _ in range(number)]
    print(len(random_numbers))
    return random_numbers


STRATEGIES = {"N": numpy_method, "I": iterative_method}


@app.command()
def generate(strategy: str, number: int):
    """Generate X number of random numbers"""

    start_time = time.perf_counter()
    print(f"Current time: {start_time} seconds")
    if strategy in STRATEGIES:
        STRATEGIES[strategy](number)
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time} seconds")


if __name__ == "__main__":
    app()
