import pytest
from professor import generate_integer, generate_number_operator

def test_generate_integer():
    assert type(generate_integer(1)) == int
    assert type(generate_integer(2)) == int
    assert type(generate_integer(3)) == int

def test_generate_integer_error():
    with pytest.raises(ValueError):
        generate_integer(0)
        generate_integer(-1)
        generate_integer(4)

def test_generate_number_operator():
    operations = generate_number_operator(3)
    assert len(operations) > 0

    for i in operations:
        assert "operation" in i 
        assert "result" in i

def test_generate_number_operator_error():
    with pytest.raises(ValueError):
        generate_number_operator(0)
        generate_number_operator(-1)
        generate_number_operator(4)

