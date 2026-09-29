from indoor import get_str

def test_indoor():
    assert get_str("HELLO") == "hello"
    assert get_str("THIS IS CS50") == "this is cs50"
    assert get_str("50") == "50"