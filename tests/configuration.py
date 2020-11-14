"""Global variables for testing."""

from pathlib import Path

import pytest

from dash_dev.doit_base import DoItGlobals

TEST_DIR: Path = Path(__file__).parent
"""Path to the `test` directory that contains this file and all other tests."""

TEST_DATA_DIR: Path = TEST_DIR / 'data'
"""Path to subdirectory with test data within the Test Directory."""

DIG_CWD: Path = TEST_DATA_DIR / 'doit_project'
"""Local directory used for testing the DoIt globals."""


@pytest.fixture()
def initialize_dig() -> DoItGlobals:
    """Initialize DoItGlobals as a fixture.

    Returns:
        DoItGlobals: DoItGlobals instance with the cwd set to `DIG_CWD`

    """
    dig = DoItGlobals()
    dig.set_paths(source_path=DIG_CWD)
    return dig
