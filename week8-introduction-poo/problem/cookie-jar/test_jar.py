from jar import Jar


def test_init():
    jar1 = Jar(5)
    assert jar1.capacity == 5


def test_str():
    jar = Jar()
    assert jar.size == ""
    jar.deposit(1)
    assert jar.size == "🍪"
    jar.deposit(11)
    assert jar.size == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

    jar = Jar(5)
    assert str(jar) == "🍪🍪🍪🍪🍪"

def test_deposit():
    jarDeposit = Jar(5)
    jarDeposit.deposit(5)
    assert jarDeposit.size == "🍪🍪🍪🍪🍪"

    try:
        jarDeposit.deposit(10)
    except ValueError as e:
        assert str(e) == f"Cannot exceed the jar's capacity of {5} cookies."


def test_withdraw():
    jarWithdraw = Jar(5)
    jarWithdraw.deposit(5)

    jarWithdraw.withdraw(2)
    jarWithdraw.size == "🍪🍪🍪"

    try:
        jarWithdraw.withdraw(4)
    except ValueError as e:
        assert str(e) == "Not enough cookies in the jar to withdraw."