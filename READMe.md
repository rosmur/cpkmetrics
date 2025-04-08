# Process Capability Metrics

***A simple utility to calculate Process Capability (Cpk) metrics.***

## Installation

### Standard Installation [Recommended]

Execute the following command in the terminal:

```bash
pip install cpkmetrics
```

NOTE: For macOS, use `pip3` if needed.

### Installation/Run with uv

Install with the uv package manager:

```bash
uv pip install cpkmetrics
```

Alternatively, you can run directly by using uv's `--with` feature.

```bash
uv run my_python_code.py --with cpkmetrics
```

### Install From Source

Clone this repo and install:

```bash
git clone
[OPTIONAL] python -m venv create?
cd cpkmetrics
pip install -e .
```

## Usage

Further examples can be found [here](examples)

## Roadmap

- Natural language results
- Skewness and Kurtosis
- Allow setting threshold values for Cpk and Cpa Ratings

## To-Do

- Need to fix process accuracy formula and ratings

### Tests

- Create a main tester. Something with all types of inputs that should pass and all types of outputs that should fail.
- Confirm setting values fails

## Contributing

Contributions are encouraged and welcome. Please note that the intent of this package is to remain very light weight, with no dependencies. Bug fixes, refactors and raising issues are highly encouraged. Please align to the design and engineering practices below and create a PR for contributions.

## Design and Engineering Practices

This project intends to have the smallest amount of code possible without sacrificing good design, structure and robust engineering practices that will allow future functionality, extensibility and forkability.

Documentation is copious - to maximize accessibility to AI/ML/SW engineers unfamiliar with statistical process control and for manufacturing/process/hardware engineers unfamiliar with python.

Project uses a modern toolchain to assist in this:

- **Project Management and Build:** pyproject.toml compliant to PEP 751 though `uv`
- **Testing:** `pytest` and `coverage`
- **Code Quality:** Linting, Formatting through `ruff` Static Analysis through `mypy`. Enforced through pre-commmit and GitHub Actions
