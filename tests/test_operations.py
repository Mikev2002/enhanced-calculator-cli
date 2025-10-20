import pytest
from app.operations import Root, Modulus, IntDivide, Percent, AbsDiff

def test_root():
    op = Root(9, 2)
    assert round(op.execute(), 2) == 3.00

def test_modulus():
    op = Modulus(10, 3)
    assert op.execute() == 1

def test_int_divide():
    op = IntDivide(10, 3)
    assert op.execute() == 3

def test_percent():
    op = Percent(50, 200)
    assert round(op.execute(), 2) == 25.00

def test_abs_diff():
    op = AbsDiff(5, 10)
    assert op.execute() == 5
