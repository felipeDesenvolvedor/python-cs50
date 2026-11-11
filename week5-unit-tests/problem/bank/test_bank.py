from bank import bank

def test_bank_hello():
    assert bank("Hello") == "$0"

def test_bank_hello_newman():
    assert bank("Hello, Newman") == "$0"

def test_bank_how():
    assert bank("How you doing?") == "$20"

def test_bank_what():
    assert bank("What's happening?") == "$100"