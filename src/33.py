def fibonacci(n):
    if n <= 0:
        return "The input is invalid."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b

# Example usage
print(fibonacci(10))  # Output: 34
