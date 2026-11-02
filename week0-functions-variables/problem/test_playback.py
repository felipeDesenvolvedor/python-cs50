from playback import get_audio

def test_get_audio():
    assert get_audio("This is CS50") == "This...is...CS50"
    assert get_audio("This is our week on functions") == "This...is...our...week...on...functions"
    assert get_audio("Let's implement a function called hello") == "Let's...implement...a...function...called...hello"