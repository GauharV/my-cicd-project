"""Tests for the calculator module."""
import pytest
from src.calculator import add, subtract, multiply, divide, power, modulo


# --- add ---

def test_add_positive_numbers():
    assert add(2, 3) == 5


def test_add_negative_numbers():
    assert add(-1, -4) == -5


def test_add_mixed_signs():
    assert add(-3, 7) == 4


def test_add_floats():
    assert add(1.5, 2.5) == pytest.approx(4.0)


def test_add_zero():
    assert add(0, 99) == 99


# --- subtract ---

def test_subtract_positive():
    assert subtract(10, 4) == 6


def test_subtract_negative_result():
    assert subtract(2, 9) == -7


def test_subtract_same_number():
    assert subtract(5, 5) == 0


def test_subtract_floats():
    assert subtract(5.5, 2.2) == pytest.approx(3.3)


# --- multiply ---

def test_multiply_positive():
    assert multiply(3, 4) == 12


def test_multiply_by_zero():
    assert multiply(99, 0) == 0


def test_multiply_negative():
    assert multiply(-3, 4) == -12


def test_multiply_both_negative():
    assert multiply(-3, -4) == 12


def test_multiply_floats():
    assert multiply(2.5, 4) == pytest.approx(10.0)


# --- divide ---

def test_divide_positive():
    assert divide(10, 2) == 5.0


def test_divide_returns_float():
    assert divide(7, 2) == pytest.approx(3.5)


def test_divide_negative():
    assert divide(-9, 3) == -3.0


def test_divide_by_zero_raises():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
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