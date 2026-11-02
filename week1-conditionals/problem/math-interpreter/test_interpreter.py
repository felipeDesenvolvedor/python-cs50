from interpreter import interpreterExpresion

def test_interpreterExpresion():
    assert interpreterExpresion("1 + 1") == "2.0"
    assert interpreterExpresion("2 - 3") == "-1.0"
    assert interpreterExpresion("2 * 2") == "4.0"
    assert interpreterExpresion("50 / 5") == "10.0"
    assert interpreterExpresion("4 / 3") == "1.3"
    assert interpreterExpresion("100 - 1") == "99.0"
    assert interpreterExpresion("-1 + 100") == "99.0"