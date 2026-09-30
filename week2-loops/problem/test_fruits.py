from fruits import get_calories

def test_get_calories():
    assert get_calories("apple") == "Portion: 242 gm = Calories 130"
    assert get_calories("avocado") == "Portion: 30 gm = Calories 50"
    assert get_calories("banana") == "Portion: 126 gm = Calories 110"
    assert get_calories("cantaloupe") == "Portion: 134 gm = Calories 50"
    assert get_calories("grapefruit") == "Portion: 154 gm = Calories 60"
    assert get_calories("grapes") == "Portion: 126 gm = Calories 90"
    assert get_calories("sweetcherries") == "Portion: 30 gm = Calories 100"