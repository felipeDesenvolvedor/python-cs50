from datetimeseasons import DateTimeSeasons

def test_get_date_born_minutes():
    assert DateTimeSeasons("1999-01-01").get_date_born_minutes() == 525600
    assert DateTimeSeasons("1999-12-31").get_date_born_minutes() == 1440
    assert DateTimeSeasons("1970-01-01").get_date_born_minutes() == 15778080

def test_get_date_born_minutes_in_words():
    assert DateTimeSeasons("1999-01-01").get_date_born_minutes_in_words() == "five hundred twenty-five thousand, six hundred"
    assert DateTimeSeasons("1999-12-31").get_date_born_minutes_in_words() == "one thousand, four hundred forty"
    assert DateTimeSeasons("1970-01-01").get_date_born_minutes_in_words() == "fifteen million, seven hundred seventy-eight thousand eighty"