"""Basic statistics module."""


def mean(numbers):
    """Return the arithmetic mean of a list of numbers."""
    if not numbers:
        raise ValueError("Cannot calculate mean of empty list")
    return sum(numbers) / len(numbers)


def maximum(numbers):
    """Return the largest value in a list."""
    if not numbers:
        raise ValueError("Cannot find maximum of empty list")
    return max(numbers)


def minimum(numbers):
    """Return the smallest value in a list."""
    if not numbers:
        raise ValueError("Cannot find minimum of empty list")
    return min(numbers)


def total(numbers):
    """Return the sum of a list of numbers."""
    return sum(numbers)
