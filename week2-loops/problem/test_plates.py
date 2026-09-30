from plates import is_valid_plate

def test_is_valid_plate():
    assert is_valid_plate("CS50") == "Valid"
    assert is_valid_plate("CS05") == "Invalid"
    assert is_valid_plate("CS50P") == "Invalid"
    assert is_valid_plate("PI3.14") == "Invalid"
    assert is_valid_plate("H") == "Invalid"
    assert is_valid_plate("OUTATIME") == "Invalid"
