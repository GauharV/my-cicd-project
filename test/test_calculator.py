import pytest
from src.calculator import add, subtract, multiply, divide

# Basic unit tests — one assertion each
def test_add():        assert add(2, 3) == 5
def test_subtract():  assert subtract(5, 3) == 2
def test_multiply():  assert multiply(3, 4) == 12
def test_divide():    assert divide(10, 2) == 5.0

# Test that an exception IS raised
def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(5, 0)


def test_divide_fraction():
    assert divide(1, 4) == pytest.approx(0.25)


# --- power ---

def test_power_positive_exponent():
    assert power(2, 10) == 1024


def test_power_zero_exponent():
    assert power(99, 0) == 1


def test_power_one_exponent():
    assert power(7, 1) == 7


def test_power_negative_exponent():
    assert power(2, -1) == pytest.approx(0.5)


# --- modulo ---

def test_modulo_basic():
    assert modulo(10, 3) == 1


def test_modulo_even_division():
    assert modulo(9, 3) == 0


def test_modulo_by_zero_raises():
    with pytest.raises(ValueError, match="Cannot modulo by zero"):
        modulo(5, 0)


def test_modulo_large_numbers():
    assert modulo(1000, 7) == 6