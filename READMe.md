# Process Capability Metrics

***A simple utility to calculate Process Capability (Cpk) metrics.***

## Roadmap

- Natural language results
- Skewness and Kurtosis
- Allow setting threshold values?

## To-Do

- Add docstrings from property methods
- Need to fix process accuracy formula and ratings
- Create enums or global vars for thresholds for cpk and cpa ratings

## Tests

- Create a main tester. Something with all types of inputs that should pass and all types of outputs that should fail.
- Confirm setting values fails

## Contributing

Contributions are encouraged and welcome. The intent of this package is to remain very light weight, with no dependencies. Please align to the design and engineering practices below and create a PR for contributions.

## Design and Engineering Practices

This project intends to have the smallest amount of code possible without sacrificing good design, structure and robust engineering practices that will allow future functionality, extensibility and forkability.

Project uses a modern toolchain to assist in this:

- **Project Management and Build:** pyproject.toml compliant to PEP 751 though `uv`
- **Testing:** `pytest` and `coverage`
- **Code Quality:** Linting, Formatting through `ruff` Static Analysis through `mypy`. Enforced through pre-commmit and GitHub Actions
