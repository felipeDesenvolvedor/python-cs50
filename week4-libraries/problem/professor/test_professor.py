import pytest
from professor import generate_int_random, generate_operations

def test_generate_integer():
    assert type(generate_int_random(1)) == int
    assert type(generate_int_random(2)) == int
    assert type(generate_int_random(3)) == int

def test_generate_integer_error():
    with pytest.raises(ValueError):
        generate_int_random(0)
        generate_int_random(-1)
        generate_int_random(4)

def test_generate_number_operator():
    operations = generate_operations(3)
    assert len(operations) > 0

    for i in operations:
        assert "operation" in i 
        assert "result" in i

def test_generate_number_operator_error():
    with pytest.raises(ValueError):
        generate_operations(0)
        generate_operations(-1)
        generate_operations(4)

