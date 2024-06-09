# flights-exploration

Tools for parsing and exploring various flights datasets.

## Installation

This library uses [poetry](https://python-poetry.org/) as a dependency manger. Please install it following the instructions on the website. Then, to install the `flights_exploration` library, you can use the following commands:

```bash
# cloning the repository
git clone git@github.com:nicolasspring/flights-exploration.git
cd flights-exploration

# install the flights_exploration library inside an virtual environment
poetry install

# activate the virtual environment
poetry shell

# you can now use the library
python3 -m flights_exploration.read  # raises AssertionError due to missing cli args
```

