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
poetry run python ctmds1/rand_nums.py country-date --for-date <date> --country-code <country_code> --granularity <granularity>
```
```
calahor76@ubuntudev:~/development/commodities_training/ctmds1$ poetry run python ctmds1/rand_nums.py country-date --for-date "2025-01-01" --country-code GB --granularity hh
{'0000': 61.062105220945114, '0030': 63.88805111738879, '0100': 70.46951577785222, '0130': 57.52272635961825, '0200': 52.898265509276946, '0230': 56.2433903196268, '0300': 52.498295282927444, '0330': 58.662683199087546, '0400': 54.61566228102327, '0430': 54.68783622792723, '0500': 52.50797702216645, '0530': 69.46034613892898, '0600': 60.17743910985692, '0630': 61.66815402372197, '0700': 65.98085846474315, '0730': 54.61978836306809, '0800': 70.85928783123077, '0830': 68.05341949442531, '0900': 58.173708391604514, '0930': 54.63268574432523, '1000': 58.35590588116611, '1030': 51.52642189689147, '1100': 58.133446332772984, '1130': 62.44867567371221, '1200': 69.82530593821883, '1230': 56.88095621253383, '1300': 55.97686372433188, '1330': 58.47051306949788, '1400': 66.03548175916973, '1430': 59.91024969007674, '1500': 53.68461802480505, '1530': 52.38492362744091, '1600': 56.16981666063763, '1630': 60.96792863043524, '1700': 67.75583145369559, '1730': 54.25268780914822, '1800': 58.33372195498802, '1830': 59.91421845441062, '1900': 66.64226182307671, '1930': 60.74684634817217, '2000': 54.44909483051181, '2030': 64.5711928649991, '2100': 53.13178589619195, '2130': 68.57450527851233, '2200': 67.32408297874238, '2230': 58.342088227139854, '2300': 58.25932244792248, '2330': 60.939639427762756}
jcalahor76@ubuntudev:~/development/commodities_training/ctmds1$ 
```