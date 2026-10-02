from tip_porcentage import get_percentage

def test_get_percentage():
    assert get_percentage("$50.00", "15%") == "Leave $7.50"
    assert get_percentage("$100.00", "18%") == "Leave $18.00"
    assert get_percentage("$15.00", "25%") == "Leave $3.75"