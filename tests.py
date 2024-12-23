import pytest
import Calculator

@pytest.fixture #creates an instance of the calculator class
def calculator():
    return Calculator.Calculator()

def test_addition(calculator):
    assert calculator.addition(2, 3) == 5 #tests addition of 2 positive numbers
    assert calculator.addition(-1, 1) == 0 #tests addition of a negative and a postive number
    assert calculator.addition(0, 0) == 0 #test addition of two 0s
    assert calculator.addition(-5, -3) == -8 #test addition of two negative numbers

def test_subtraction(calculator):
    assert calculator.subtraction(5, 3) == 2  # tests subtraction of 2 positive numbers
    assert calculator.subtraction(-1, 1) == -2  # tests subtraction of a positive from a negative number
    assert calculator.subtraction(0, 0) == 0  # tests subtraction of two 0s
    assert calculator.subtraction(-5, -3) == -2  # tests subtraction of two negative numbers

def test_multiplication(calculator):
    assert calculator.multiplication(2, 3) == 6  # tests multiplication of 2 positive numbers
    assert calculator.multiplication(-1, 1) == -1  # tests multiplication of a negative and a positive number
    assert calculator.multiplication(0, 5) == 0  # tests multiplication by 0
    assert calculator.multiplication(-2, -3) == 6  # tests multiplication of two negative numbers

def test_division(calculator):
    assert calculator.division(6, 3) == 2  # tests division of 2 positive numbers
    assert calculator.division(-6, 3) == -2  # tests division of a negative by a positive number
    assert calculator.division(-6, -3) == 2  # tests division of two negative numbers
    assert calculator.division(0, 5) == 0  # tests division of 0 by a positive number
    # tests division by zero raises ValueError
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculator.division(5, 0)




