from deep import valid_input

def test_valid_input():
    assert valid_input("42") == "Yes" 
    assert valid_input(" 42 ") == "Yes" 
    assert valid_input("Forty Two") == "Yes" 
    assert valid_input("forty-two") == "Yes" 
    assert valid_input("50") == "No" 