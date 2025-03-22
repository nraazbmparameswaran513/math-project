def add_numbers(x, y):
    """
    Add two numbers x and y.
    
    Parameters:
        x (int/float): The first number.
        y (int/float): The second number.
        
    Returns:
        int/float: The sum of x and y.
    """
    return x + y

def subtract_numbers(x, y):
    """
    Subtract two numbers x from y.
    
    Parameters:
        x (int/float): The first number.
        y (int/float): The second number.
        
    Returns:
        int/float: The result of the subtraction.
    """
    return x - y

def multiply_numbers(x, y):
    """
    Multiply two numbers x and y.
    
    Parameters:
        x (int/float): The first number.
        y (int/float): The second number.
        
    Returns:
        int/float: The product of x and y.
    """
    return x * y

def divide_numbers(x, y):
    """
    Divide two numbers x by y.
    
    Parameters:
        x (int/float): The numerator.
        y (int/float): The denominator.
        
    Returns:
        int/float: The quotient of x divided by y.
    """
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

def calculate(expression):
    """
    Evaluate an arithmetic expression given a string.

    Parameters:
        expression (str): A mathematical expression in string format.

    Returns:
        float: The result of the evaluated expression.
    """
    try:
        # Parsing the expression
        parts = expression.split(' ')
        numbers = []
        operators = []

        for part in parts:
            if part.isdigit():
                numbers.append(int(part))
            elif part == 'x' or part == 'y':
                operators.append(part)
            else:
                raise ValueError("Invalid operator: " + part)

        # Apply the operations
        result = add_numbers(numbers[0], numbers[-1])
        for i in range(1, len(numbers) - 1):
            if operators[i-1] == '+' or operators[i-1] == '-':
                operation = f'{operators[i-1]} {numbers[i-1]}'
                operator_to_multiply = numbers[i]
                result += subtract_numbers(number)
                return result

    except ValueError as e:
        print(f"Error: {e}")
        return None

# Example usage
expression = "3 + 5 * x / y"
result = calculate(expression)
print(result)
