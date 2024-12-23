# Disclaimer
- This is a python application that calculates the sum, the subtraction, the multiplication and the division of two numbers. 
- The tool used for automation testing is pytest. 
- This is an entirely separate file from the project.

---

# Overview

The application that the automation is made for is a `Calculator app`, which provides the basic arithmetic operations (`addition`, `subtraction`, `multiplication` and `division`). 
The tests ensure that these operations work as intended, under the given circumstances (see the tests below).

---

# Files
### 1. `tests.py`
This file contains the test cases for the `Calculator` class.
Run this file to run the tests.

### 2. `Calculator.py`
This file contains the implementation of the `Calculator` class, which includes the following methods:
- `addition(a, b)`: Adds two numbers.
- `subtraction(a, b)`: Subtracts the second number from the first.
- `multiplication(a, b)`: Multiplies two numbers.
- `division(a, b)`: Divides the first number by the second and raises a `ValueError` if the divisor is zero.

---

# Test Cases

### 1. **Addition**
- Adds two positive numbers.
- Adds a negative and a positive number.
- Adds two zeros.
- Adds two negative numbers.

### 2. **Subtraction**
- Subtracts two positive numbers.
- Subtracts a positive number from a negative number.
- Subtracts two zeros.
- Subtracts two negative numbers.

### 3. **Multiplication**
- Multiplies two positive numbers.
- Multiplies a negative and a positive number.
- Multiplies two.
- Multiplies two negative numbers.
- Multiplies by zero.

### 4. **Division**
- Divides two positive numbers.
- Divides a negative number by a positive number.
- Divides two negative numbers.
- Divides zero by a positive number.
- Validates that dividing by zero raises a `ValueError` with the correct error message.
