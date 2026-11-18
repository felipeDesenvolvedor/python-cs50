import pytest
from professor import generate_integer, generate_operations

def test_generate_integer():
    assert type(generate_integer(1)) == int
    assert type(generate_integer(2)) == int
    assert type(generate_integer(3)) == int

def test_generate_number_operator():
    operations = generate_operations(3)
    assert len(operations) > 0

    for i in operations:
        assert "operation" in i 
        assert "result" in i

