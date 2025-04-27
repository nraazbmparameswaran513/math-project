def multiply_two_numbers(a: float, b: float) -> float:
    """
    This function multiplies two numbers and returns the result.
    
    Args:
        a (float): The first number to be multiplied.
        b (float): The second number to be multiplied.
        
    Returns:
        float: The product of `a` and `b`.
    """
    return a * b

def main():
    # Example usage
    num1 = 5.0
    num2 = 3.0
    result = multiply_two_numbers(num1, num2)
    print(f"The result of multiplying {num1} and {num2} is: {result}")
    
if __name__ == "__main__":
    main()
