from twttr import shorten

def test_shorten():
    assert shorten("FElIpE dA SIlvA") == "Flp d Slv"
    assert shorten("What's your name?") == "Wht's yr nm?"
    assert shorten("CS50") == "CS50"