# ctmds1: Random Number Generator

A Python application for generating random numbers, powered by **Poetry** for dependency management, **Ruff** for linting, and a **Makefile** for automation.

## Prerequisites

Ensure you have the following tools installed on your system:

- **Python** (3.x)
- **Poetry**: For managing dependencies and packaging.
- **Make**: For automating tasks.
- **Ruff**: For linting your code.

You can install Poetry by following the instructions at [Poetry Installation Guide](https://python-poetry.org/docs/#installation).

## Project Setup

To get started with the project:

1. Clone the repository:

    ```bash
    git clone <repository-url>
    cd ctmds1
    ```

2. Install project dependencies with Poetry:

    ```bash
    poetry install
    ```

3. Activate the Poetry virtual environment (Poetry automatically handles this):

    ```bash
    poetry shell
    ```

## Running the Application

The main command-line interface (CLI) is powered by **Typer**. You can use it to generate random numbers by running the following command:

```bash
poetry run python ctmds1/rand_nums.py generate --number 100
```


```bash
poetry run python main.py country_date --for-date YYYY-MM-DD --country-code COUNTRY_CODE [--granularity h|hh]
```

Arguments:

--for-date (required): The date in YYYY-MM-DD format.
--country-code (required): The country code (GB, FR, NL, DE).
--granularity (optional, default: h): The granularity of data.
    h: Hourly data (24 values for normal days, 23/25 for DST days).
    hh: Half-hourly data (48 values for normal days, 46/50 for DST days).

```
jcalahor76@ubuntudev:~/development/commodities_training/ctmds1$ poetry run python ctmds1/rand_nums.py --commodity crude --for-date "2024-11-03" --country GB --granularity hh
25
{'0000': 59.92, '0030': 60.04, '0100': 81.51, '0130': 66.32, '0200': 63.81, '0230': 76.4, '0300': 73.83, '0330': 78.57, '0400': 72.15, '0430': 79.11, '0500': 81.28, '0530': 80.39, '0600': 84.79, '0630': 84.76, '0700': 87.04, '0730': 78.78, '0800': 80.3, '0830': 75.49, '0900': 74.1, '0930': 75.82, '1000': 69.31, '1030': 63.87, '1100': 84.12, '1130': 64.49, '1200': 58.8, '1230': 52.47, '1300': 75.52, '1330': 72.16, '1400': 83.95, '1430': 76.31, '1500': 70.76, '1530': 73.44, '1600': 66.07, '1630': 69.67, '1700': 67.31, '1730': 84.48, '1800': 92.33, '1830': 76.39, '1900': 65.11, '1930': 62.25, '2000': 73.41, '2030': 77.51, '2100': 74.37, '2130': 69.13, '2200': 72.38, '2230': 85.85, '2300': 83.02, '2330': 61.84, '2400': 66.63, '2430': 78.66}
jcalahor76@ubuntudev:~/development/commodities_training/ctmds1$ 
```
