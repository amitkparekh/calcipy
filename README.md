# Dash_Dev ([Github](https://github.com/KyleKing/dash_dev))

Python package to simplify development. Includes functionality for task running, testing, linting, documenting, and more

Note: the package name is a misnomer and is not specific to Plotly/Dash projects (and I haven't thought of a better replacement yet). If you want to build Plotly/Dash applications, see [dash_charts](https://github.com/KyleKing/dash_charts)

## Quick Start

<!-- TODO: Replace with CookieCutter Instructions -->

Add to a poetry project in `pyproject.toml`:

```toml
[tool.poetry.dev-dependencies.dash_dev]
git = "https://github.com/KyleKing/dash_dev.git"
branch = "main"
```

Then copy the [`https://github.com/KyleKing/dash_dev/blob/master/dodo.py`](https://github.com/KyleKing/dash_dev/blob/master/dodo.py) file into your project and call with `poetry run doit`

If you have any questions, please [open an issue on Github](https://github.com/KyleKing/dash_dev/issues/new)

## Where Used

- [KyleKing/dash_charts](https://github.com/KyleKing/dash_charts)
- [KyleKing/PiAlarm](https://github.com/KyleKing/PiAlarm)
- [KyleKing/Kitsu_Library_Availability](https://github.com/KyleKing/Kitsu_Library_Availability)
- [KyleKing/Goodreads_Library_Availability](https://github.com/KyleKing/Goodreads_Library_Availability) - *Planned*

## Test Coverage

<!-- COVERAGE -->

| File | Statements | Missing | Excluded | Coverage |
| --: | --: | --: | --: | --: |
| `dash_dev/__init__.py` | 11 | 0 | 0 | 100.0% |
| `dash_dev/conftest.py` | 23 | 3 | 0 | 87.0% |
| `dash_dev/doit_helpers/__init__.py` | 0 | 0 | 0 | 100.0% |
| `dash_dev/doit_helpers/base.py` | 98 | 14 | 0 | 85.7% |
| `dash_dev/doit_helpers/dev.py` | 44 | 44 | 0 | 0.0% |
| `dash_dev/doit_helpers/doc.py` | 135 | 78 | 0 | 42.2% |
| `dash_dev/doit_helpers/lint.py` | 80 | 19 | 0 | 76.2% |
| `dash_dev/doit_helpers/test.py` | 39 | 13 | 0 | 66.7% |
| `dash_dev/log_helpers.py` | 24 | 5 | 0 | 79.2% |
| `dash_dev/registered_tasks.py` | 6 | 6 | 0 | 0.0% |
| `dash_dev/tag_collector.py` | 70 | 16 | 0 | 77.1% |

Generated on: 2020-11-14T10:32:35.579431

<!-- /COVERAGE -->
