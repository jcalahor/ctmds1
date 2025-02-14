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
jcalahor76@ubuntudev:~/development/commodities_training/ctmds1$ poetry run python ctmds1/rand_nums.py country-date --for-date "2024-11-03" --country-code GB --granularity hh
25
{'0000': 70.63730894096003, '0030': 59.33339584562105, '0100': 64.83058325400556, '0130': 59.95244260359641, '0200': 55.40696964889092, '0230': 57.73689802574573, '0300': 62.6007607453393, '0330': 54.85297927545298, '0400': 59.28337896962822, '0430': 55.60210432341202, '0500': 67.77322058828375, '0530': 68.51383648007062, '0600': 56.198327174697816, '0630': 66.5337032566783, '0700': 66.45021968641458, '0730': 57.96049707909561, '0800': 64.32727065885508, '0830': 67.95294965125956, '0900': 63.0580898322085, '0930': 67.94372006181526, '1000': 58.74402276869546, '1030': 69.64971402516446, '1100': 53.58360724559373, '1130': 67.33018558428873, '1200': 64.58072655706523, '1230': 58.082931006074524, '1300': 68.42061544707424, '1330': 56.44184373875636, '1400': 66.07916059844797, '1430': 65.25929048648054, '1500': 62.023968004166505, '1530': 53.18809321934237, '1600': 62.641271739964424, '1630': 55.80666544684174, '1700': 64.2927694128143, '1730': 70.67857789697112, '1800': 61.19171049828506, '1830': 55.44646324726355, '1900': 60.723802055825246, '1930': 56.781572825972546, '2000': 53.578118939308716, '2030': 55.748733174775026, '2100': 51.02599584561778, '2130': 62.499314552731796, '2200': 66.26135951059791, '2230': 67.9264947410349, '2300': 69.75810600956154, '2330': 70.39524120244707, '2400': 68.171967190965, '2430': 63.741737024838436}
jcalahor76@ubuntudev:~/development/commodities_training/ctmds1$ 
```
