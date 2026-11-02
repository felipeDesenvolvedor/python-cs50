from outdated import convert_outdated

def test_convert_outdated():
    assert convert_outdated("9/8/1636") == "1636-09-08"
    assert convert_outdated("September 8, 1636") == "1636-09-08"
    assert convert_outdated("8/9/1636") == "1636-08-09"
    assert convert_outdated("1/1/1970") == "1970-01-01"
    assert convert_outdated("January 1, 1970") == "1970-01-01"