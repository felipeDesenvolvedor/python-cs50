from grocery import return_grocery

def test_return_grocery():
    assert return_grocery(['apple', 'banana', 'banana', 'ice cream']) == '1 APPLE \n2 BANANA \n1 ICE CREAM '