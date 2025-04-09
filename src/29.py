import random

def generate_random_string(length):
    """Generate a random string of specified length."""
    return ''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(length))

random_string = generate_random_string(10)
print(random_string)
