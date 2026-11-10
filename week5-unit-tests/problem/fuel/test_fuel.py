import pytest
from fuel import gauge, convert

def test_gauge_e():
    assert gauge(0) == "<E>"
    assert gauge(1) == "<E>"

def test_gauge_f():
    assert gauge(99) == "<F>"
    assert gauge(100) == "<F>"

def test_gauge_middle():
    assert gauge(10) == "10%"
    assert gauge(50) == "50%"
    assert gauge(90) == "90%"

def test_convert():
    assert convert("3", "4") == 75
    assert convert("1", "4") == 25
    assert convert("4", "4") == 100
    assert convert("0", "4") == 0

def test_convert_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("4", "0")

def test_convert_negative_numbers():
    with pytest.raises(ValueError):
        convert("-4", "-2")

def test_convert_x_greater_y():
    with pytest.raises(ValueError):
        convert("10", "5")

def test_convert_no_integer():
    with pytest.raises(ValueError):
        convert("5.5", "10")
    with pytest.raises(ValueError):
        convert("5", "10.55")