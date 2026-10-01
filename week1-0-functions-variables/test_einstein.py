from einstein import get_joules

def test_einstein():
    assert get_joules(1) == 90000000000000000
    assert get_joules(14) == 1260000000000000000
    assert get_joules(50) == 4500000000000000000