# This is a simple example to demonstrate how Python can be used as a mathematical tool.
# It performs basic arithmetic operations like addition, subtraction, multiplication, and division.

def add(a, b):
    """Perform addition"""
    return a + b

def subtract(a, b):
    """Perform subtraction"""
    return a - b

def multiply(a, b):
    """Perform multiplication"""
    return a * b

def divide(a, b):
    """Perform division"""
    if b != 0:
        return a / b
    else:
        raise ValueError("Cannot divide by zero")

# Example usage:
result1 = add(5, 3)
print(f"Addition: {result1}")

result2 = subtract(10, 4)
print(f"Subtraction: {result2}")

result3 = multiply(7, 2)
print(f"Multiplication: {result3}")

try:
    result4 = divide(10, 0)
except ValueError as e:
    print(e)

