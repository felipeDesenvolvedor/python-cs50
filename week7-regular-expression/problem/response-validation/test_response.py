from response import validat_email

def test_validat_email():
    assert validat_email("malan@harvard.edu") == "Valid"
    assert validat_email("felipedasilvasantos30@gmail.com") == "Valid"

def test_invalidat_email():
    assert validat_email("malan@@@harvard.edu") == "Invalid"
    assert validat_email("felipedasilvasantos30@gmail..com") == "Invalid"
