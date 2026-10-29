from meal import convert

def test_convert():
    assert convert("7:00") == "breakfast time"
    assert convert("7:30") == "breakfast time"
    assert convert("8:00") == "breakfast time"
    assert convert("12:42") == "lunch time"
    assert convert("18:32") == "dinner time"
    assert convert("11:11") == None