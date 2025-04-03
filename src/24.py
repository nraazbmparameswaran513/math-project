def find_largest_prime_factor(n):
    """
    Find the largest prime factor of a given number n.
    
    Parameters:
    n (int): The number to find the largest prime factor of.
    
    Returns:
    int: The largest prime factor of n.
    """
    if n % 2 == 0:
        return 2
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return i
    return n

# Example usage
number = 60
print("The largest prime factor of", number, "is:", find_largest_prime_factor(number))
