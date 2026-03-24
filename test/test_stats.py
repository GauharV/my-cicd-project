"""Tests for the stats module.

Demonstrates:
  - Fixtures (from conftest.py)
  - parametrize
  - Markers
  - Coverage enforcement
"""
import pytest

from src.stats import mean, maximum, minimum, total


# ---------------------------------------------------------------
# 1. FIXTURES
# Fixtures are injected by name — pytest matches the parameter
# name to a fixture defined in conftest.py or this file.
# ---------------------------------------------------------------

def test_mean_with_fixture(sample_numbers):
    """Uses the sample_numbers fixture from conftest.py."""
    assert mean(sample_numbers) == 3.0


def test_total_with_fixture(sample_numbers):
    """Fixture is reused across tests — each gets a fresh copy."""
    assert total(sample_numbers) == 15


def test_mean_empty_raises(empty_list):
    """Empty-list fixture keeps edge cases readable."""
    with pytest.raises(ValueError, match="empty list"):
        mean(empty_list)


def test_maximum_empty_raises(empty_list):
    with pytest.raises(ValueError, match="empty list"):
        maximum(empty_list)


def test_minimum_empty_raises(empty_list):
    with pytest.raises(ValueError, match="empty list"):
        minimum(empty_list)


def test_mean_negatives(negative_numbers):
    """Fixture with negative values — mean of [-10,-3,-1,0,2]."""
    assert mean(negative_numbers) == pytest.approx(-2.4)


def test_large_dataset_mean(large_dataset):
    """Module-scoped fixture: setup runs once for this whole file."""
    assert mean(large_dataset) == pytest.approx(50.5)


def test_large_dataset_total(large_dataset):
    """Second test reuses the same module-scoped fixture instance."""
    assert total(large_dataset) == 5050


# ---------------------------------------------------------------
# 2. PARAMETRIZE
# One test function, many input/output pairs.
# pytest runs it once per row and labels each run clearly.
# ---------------------------------------------------------------

@pytest.mark.parametrize("numbers, expected", [
    ([1, 2, 3], 2.0),
    ([10, 20, 30], 20.0),
    ([0, 0, 0], 0.0),
    ([-5, 5], 0.0),
    ([7], 7.0),
])
def test_mean_parametrized(numbers, expected):
    """Runs 5 independent test cases from a single function."""
    assert mean(numbers) == pytest.approx(expected)


@pytest.mark.parametrize("numbers, expected", [
    ([3, 1, 4, 1, 5], 5),
    ([-1, -5, -2], -1),
    ([42], 42),
])
def test_maximum_parametrized(numbers, expected):
    assert maximum(numbers) == expected


@pytest.mark.parametrize("numbers, expected", [
    ([3, 1, 4, 1, 5], 1),
    ([-1, -5, -2], -5),
    ([42], 42),
])
def test_minimum_parametrized(numbers, expected):
    assert minimum(numbers) == expected


@pytest.mark.parametrize("numbers, expected", [
    ([1, 2, 3, 4], 10),
    ([], 0),
    ([-1, 1], 0),
    ([100], 100),
])
def test_total_parametrized(numbers, expected):
    assert total(numbers) == expected


# ---------------------------------------------------------------
# 3. MARKERS
# @pytest.mark.slow  — excluded from standard CI runs
# @pytest.mark.external — excluded from standard CI runs
# Both are registered in pytest.ini to avoid warnings.
# Run them manually: pytest -m slow
# ---------------------------------------------------------------

@pytest.mark.slow
def test_mean_very_large_list():
    """Marked slow — skipped in CI with: pytest -m 'not slow'."""
    big = list(range(1_000_000))
    assert mean(big) == pytest.approx(499999.5)


@pytest.mark.external
def test_external_placeholder():
    """Marked external — would call a live API in a real project.
    Skipped in CI with: pytest -m 'not external'
    Run manually with: pytest -m external
    """
    # Simulated — real version would do: requests.get(...)
    assert True
