from bank import bank_tip

def test_bank_tip():
    assert bank_tip("Hello") == "$0"
    assert bank_tip("Hello, Newman") == "$0"
    assert bank_tip("How you doing?") == "$20"
    assert bank_tip("What's happening?") == "$100"