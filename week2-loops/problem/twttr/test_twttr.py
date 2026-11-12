from twttr import get_twttr

def test_twttr():
    assert get_twttr("Twitter") == "Twttr"
    assert get_twttr("What's your name?") == "Wht's yr nm?"
    assert get_twttr("CS50") == "CS50"