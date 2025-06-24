# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2025-04-09

Initial release of cpkmetrics, a featherweight Python library for calculating process capability metrics.

### Added
- Core process capability calculation functionality with zero dependencies, computing the following metrics
    - Cp (Process Capability)
    - Cpk (Process Capability Index, adjusted for mean shift)
    - Cpu (Upper Process Capability Index)
    - Cpl (Lower Process Capability Index)
    - Cpa (Process Accuracy)
    - Process Sigma Level
    - Cpk and Cpa Ratings
- Examples for:
    - Basic usage with numeric inputs
    - Accessing results through output attributes and dictionaries
    - Dataframe compatibility (and by extension CSVs)
- Comprehensive docstrings and documentation
- Full test coverage
- Type hints with mypy validation
- Code quality enforced through ruff
- Modern toolchain with pyproject.toml and uv support

[0.1.0]: https://github.com/rosmur/cpkmetrics/releases/tag/v0.1.0