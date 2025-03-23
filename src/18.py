def add_numbers(a, b):
    """
    Add two numbers and return the result.
    
    Parameters:
    a (int): First number to be added.
    b (int): Second number to be added.
    
    Returns:
    int: The sum of a and b.
    """
    return a + b

def subtract_numbers(a, b):
    """
    Subtract two numbers and return the result.
    
    Parameters:
    a (int): First number to be subtracted from.
    b (int): Second number to be subtracted from.
    
    Returns:
    int: The difference between a and b.
    """
    return a - b

def multiply_numbers(a, b):
    """
    Multiply two numbers and return the result.
    
    Parameters:
    a (int): First number to be multiplied.
    b (int): Second number to be multiplied.
    
    Returns:
    int: The product of a and b.
    """
    return a * b

def divide_numbers(a, b):
    """
    Divide two numbers and return the result.
    
    Parameters:
    a (int): First number to be divided from.
    b (int): Second number to be divided with.
    
    Returns:
    float: The quotient of a and b.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def calculate_squares(numbers):
    """
    Calculate the squares of each number in the list and return a new list containing those squares.
    
    Parameters:
    numbers (list): A list of integers or floats to be squared.
    
    Returns:
    list: A new list containing the squares of the input numbers.
    """
    result = []
    for num in numbers:
        result.append(num ** 2)
    return result

def calculate_cube(numbers):
    """
    Calculate the cubes of each number in the list and return a new list containing those cubes.
    
    Parameters:
    numbers (list): A list of integers or floats to be cubed.
    
    Returns:
    list: A new list containing the cubes of the input numbers.
    """
    result = []
    for num in numbers:
        result.append(num ** 3)
    return result

def calculate_square_root(numbers):
    """
    Calculate the square root of each number in the list and return a new list containing those square roots.
    
    Parameters:
    numbers (list): A list of integers or floats to be squared rooted.
    
    Returns:
    list: A new list containing the square roots of the input numbers.
    """
    result = []
    for num in numbers:
        result.append(num ** 0.5)
    return result

def calculate_logarithms(numbers, base):
    """
    Calculate the logarithm of each number in the list to a given base and return a new list containing those results.
    
    Parameters:
    numbers (list): A list of integers or floats to be transformed into their logarithms with the specified base.
    base (float): The base which will be raised to make the exponentiations.
    
    Returns:
    list: A new list containing the logarithm values of the input numbers, each multiplied by the given base.
    """
    result = []
    for num in numbers:
        result.append(log(num, base))
    return result

def main():
    user_input = input("Enter a number or multiple numbers separated by spaces:")
    
    if "," in user_input:
        nums = [float(x) for x in user_input.split(",")]
    else:
        nums = [int(x) for x in user_input]
    
    print("\nNumbers entered: ", nums)
    
    add_func = add_numbers
    subtract_func = subtract_numbers
    multiply_func = multiply_numbers
    divide_func = divide_numbers
    square_func = calculate_squares
    cube_func = calculate_cube
    sqrt_func = calculate_square_root
    log_func = calculate_logarithms
    
    user_input = input("Enter a number or multiple numbers separated by spaces:")
    
    if "," in user_input:
        nums = [float(x) for x in user_input.split(",")]
    else:
        nums = [int(x) for x in user_input]
    
    print("\nInput Numbers: ", nums)
    
    operation = input("Enter an arithmetic operation (+, -, *, /): ")
    
    if operation == "+" or operation == "-" or operation == "*" or operation == "/" or operation == "**":
        if operation in ["*", "/"]:
            result = [operation, user_input].pop(0) + [user_input]
        else:
            if not numbers:
                print("No input values provided.")
                return
            result = list(map(operation, numbers))
    elif operation == "log" or operation == "exp":
        result = calculate_logarithms(user_input, 10)
    elif operation == "sqrt":
        result = sqrt_func(numbers)
    else:
        if not numbers:
            print("No input values provided.")
            return
        result = list(map(operation, numbers))
    
    print("\nResult: ", result)

if __name__ == "__main__":
    main()
