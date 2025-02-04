## Random Number Generator (Source Code)

This repository provides the source code for a command-line tool to generate random numbers using two different strategies: Numpy-based and Iterative. It utilizes `typer` for building the command-line interface (CLI) and `numpy` for fast number generation.

### Project Structure:

```src/
├── generator.py      # Contains the random number generation methods
├── main.py           # Main entry point for the CLI application
└── README.md         # Project documentation
```

`generator.py`

This file contains two random number generation methods:
- `numpy_method(number: int)`: Uses Numpy to generate `number` of random numbers between 1 and 100.
- `iterative_method(number: int)`: Uses a Python list comprehension and the `random` module to generate `number` of random numbers.

This is the main entry point for the CLI tool using `typer`. It exposes a command `generate` that allows the user to choose between the two strategies (Numpy or Iterative) and specify the number of random numbers to generate.

### Installation

To install and use the project locally:

1. Clone the repository (if applicable):

   git clone <repository_url>
   cd <project_directory>

2. Create and activate a virtual environment:

   On macOS/Linux:
     python3 -m venv venv
     source venv/bin/activate

   On Windows:
     python -m venv venv
     venv\Scripts\activate

3. Install dependencies:

   Install the required Python packages:

   pip install -r requirements.txt

   If you don't have a requirements.txt, manually install the required dependencies:

   pip install typer numpy

### Usage

After setting up the environment, you can use the command-line interface to generate random numbers.

Command Syntax:

   python src/main.py generate --strategy <strategy> --number <number>

Options:
- --strategy: Specifies the strategy for generating random numbers. You can choose between:
    - `N`: Numpy-based random number generation.
    - `I`: Iterative method for generating random numbers.
- --number: The number of random numbers to generate.

### Example Commands:

1. Generate 10 random numbers using the Numpy method:

   ```python src/main.py generate --strategy N --number 10

   Output:
   Current time: 1675277681.512604 seconds
   10
   Elapsed time: 0.001234567 seconds
   ```

2. Generate 10 random numbers using the Iterative method:

   ```python src/main.py generate --strategy I --number 10

   Output:
   Current time: 1675277681.712604 seconds
   10
   Elapsed time: 0.002345678 seconds
   ```

Options:

- `--strategy`: Choose `N` for Numpy-based generation or `I` for the Iterative method.
- `--number`: The number of random numbers you want to generate.


### Tests:

```
pytest tests/
```

