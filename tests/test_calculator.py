import pytest
from calculator import calculate


def test_addition():
    result, duration = calculate(3, 9, "plus")
    assert result == 12
    assert duration >= 0  


def test_subtraction():
    result, _ = calculate(10, 4, "minus")
    assert result == 6


def test_multiplication():
    result, _ = calculate(5, 6, "multiply")
    assert result == 30


def test_division():
    result, _ = calculate(8, 2, "divide")
    assert result == 4


def test_addition_with_floats():
    result, _ = calculate(1.5, 2.5, "plus")
    assert result == 4.0


def test_divide_by_zero_raises():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculate(10, 0, "divide")


def test_invalid_operation_raises():
    with pytest.raises(ValueError, match="Invalid operation"):
        calculate(1, 2, "banana")

def test_returns_tuple_of_result_and_duration():
    output = calculate(2, 2, "plus")
    assert isinstance(output, tuple)
    assert len(output) == 2
    result, duration = output
    assert result == 4
    assert isinstance(duration, float)
