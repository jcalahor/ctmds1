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

```
jcalahor76@ubuntudev:~/development/commodities_training/ctmds1$ poetry run uvicorn ctmds1.api:app --host 0.0.0.0 --port 8000 --reload
```

Connecting to the API
```
$ curl -X GET "http://192.168.9.183:8000/country-date/crude/2024-02-24/GB/h" -H "Accept: application/json"
{"prices":{"0000":47.18,"0100":51.0,"0200":52.39,"0300":66.32,"0400":67.53,"0500":52.36,"0600":73.01,"0700":62.01,"0800":69.01,"0900":57.1,"1000":63.03,"1100":61.38,"1200":46.28,"1300":53.69,"1400":58.12,"1500":53.39,"1600":54.19,"1700":64.33,"1800":68.09,"1900":58.42,"2000":57.82,"2100":61.55,"2200":60.7,"2300":64.25}}$ 
```
