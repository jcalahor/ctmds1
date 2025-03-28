# Use official Python 3.12 slim image
FROM python:3.12-slim

ARG YOUR_ENV

ENV YOUR_ENV=${YOUR_ENV} \
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  # Poetry's configuration:
  POETRY_NO_INTERACTION=1 \
  POETRY_VIRTUALENVS_CREATE=false \
  POETRY_CACHE_DIR='/var/cache/pypoetry' \
  POETRY_HOME='/usr/local' \
  POETRY_VERSION=1.7.1
  # ^^^
  # Make sure to update it!

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Set working directory
WORKDIR /app

# Copy pyproject.toml and poetry.lock first for dependency installation
COPY pyproject.toml poetry.lock* ./

RUN poetry --version
# Install dependencies without creating a virtual environment
RUN poetry install --no-interaction --no-ansi

# Copy project files
COPY . .

# Expose FastAPI port
EXPOSE 8000

# Run FastAPI with --reload enabled
CMD ["poetry", "run", "uvicorn", "ctmds1.api:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
