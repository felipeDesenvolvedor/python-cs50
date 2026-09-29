from camel_case import get_snack_case


def test_get_snack_case():
    assert get_snack_case("camelCase") == "camel_case"
    assert get_snack_case("firstName") == "first_name"
    assert get_snack_case("preferredFirstName") == "preferred_first_name"