from working import convert

def test_convert():
    assert convert("9:00 AM to 5:00 PM") == "Valid"
    assert convert("9 AM to 5 PM") == "Valid"
    assert convert("9:00 AM to 5 PM") == "Valid"
    assert convert("9 AM to 5:00 PM") == "Valid"
    assert convert("10 AM to 8:50 PM") == "Valid"
    assert convert("10:30 PM to 8 AM") == "Valid"

def test_convert_error():
    try:
        convert("9:00 A 5:00 PM")
    except ValueError as e:
        assert e == "Invalid"
    try:
        convert("9 AM - 5 PM")
    except ValueError as e:
        assert e == "Invalid"
    try:
        convert("09:00 AM - 17:00 PM")
    except ValueError as e:
        assert e == "Invalid"
    try:
        convert("9:60 AM to 5:60 PM")
    except ValueError as e:
        assert e == "Invalid"