from nutrition import get_calories

def test_get_calories():
    assert get_calories("apple") == "Calories: 130"
    assert get_calories("avocado") == "Calories: 50"
    assert get_calories("banana") == "Calories: 110"
    assert get_calories("cantaloupe") == "Calories: 50"
    assert get_calories("grapefruit") == "Calories: 60"
    assert get_calories("grapes") == "Calories: 90"
    assert get_calories("sweetcherries") == "Calories: 100"