"""Shared pytest fixtures for the test suite.

Fixtures defined here are automatically available to every test file
without needing to import them — pytest discovers conftest.py files
by walking up the directory tree.
"""
import pytest


# --- Scope: function (default) ---
# A fresh instance is created before EACH test that uses it.

@pytest.fixture
def sample_numbers():
    """Return a standard list of integers used across many tests."""
    return [1, 2, 3, 4, 5]


@pytest.fixture
def empty_list():
    """Return an empty list for edge-case tests."""
    return []


@pytest.fixture
def negative_numbers():
    """Return a list containing negative values."""
    return [-10, -3, -1, 0, 2]


# --- Scope: module ---
# Created once per test FILE that uses it (faster for expensive setup).

@pytest.fixture(scope="module")
def large_dataset():
    """Return a larger dataset — created once per module."""
    return list(range(1, 101))  # [1, 2, ..., 100]
