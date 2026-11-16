from grocery import return_grocery

def test_return_grocery():
    assert return_grocery(['apple', 'banana', 'banana', 'ice cream']) == '1 APPLE\n1 ICE CREAM\n2 BANANA'
    assert return_grocery(['mango', 'strawberry']) == '1 MANGO\n1 STRAWBERRY'
    assert return_grocery(['milk', 'milk']) == '2 MILK'
    assert return_grocery(['tortilla', 'sweet potato']) == '1 SWEET POTATO\n1 TORTILLA' 
    assert return_grocery(["mango", "sugar", "mango"]) == '1 SUGAR\n2 MANGO' 