import pytest
from app.calculator import Calculator

@pytest.fixture
def calc():
    return Calculator()

def test_add(calc):
    result = calc.calculate("add", 2, 3)
    assert result == 5

def test_subtract(calc):
    result = calc.calculate("subtract", 5, 2)
    assert result == 3

def test_multiply(calc):
    result = calc.calculate("multiply", 3, 4)
    assert result == 12

def test_divide(calc):
    result = calc.calculate("divide", 10, 2)
    assert result == 5

def test_divide_by_zero(calc):
    with pytest.raises(ZeroDivisionError):
        calc.calculate("divide", 10, 0)

def test_power(calc):
    result = calc.calculate("power", 2, 3)
    assert result == 8

def test_undo_redo(calc):
    calc.calculate("add", 1, 1)
    calc.calculate("multiply", 2, 3)
    assert len(calc.get_history()) == 2

    calc.undo()
    assert len(calc.get_history()) == 1

    calc.redo()
    assert len(calc.get_history()) == 2
