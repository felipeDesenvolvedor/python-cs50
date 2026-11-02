from deep import valid_input

def test_valid_input():
    assert valid_input("42") == True 
    assert valid_input("Forty Two") == True 
    assert valid_input("forty-two") == True 
    assert valid_input("50") == "No" 