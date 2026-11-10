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