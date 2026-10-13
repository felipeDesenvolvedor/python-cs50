from datetimeseasons import DateTimeSeasons

def test_get_date_born_minutes():
    assert DateTimeSeasons("1996-05-21").get_date_born_minutes() == 15986880

def test_get_date_born_minutes_in_words():
    assert DateTimeSeasons("1996-05-21").get_date_born_minutes_in_words() == "fifteen million, nine hundred eighty-six thousand, eight hundred eighty"