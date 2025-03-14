import random
def get_random_number(n):
    if n < 1:
        raise ValueError("n must be greater than or equal to 1")
    return random.randint(1, n)
def get_random_name():
    names = ["Alice", "Bob", "Charlie", "David", "Eve"]
    return random.choice(names)
def get_random_boolean():
    return random.choice([True, False])
def get_random_string(n):
    if n < 1:
        raise ValueError("n must be greater than or equal to 1")
    return "".join(chr(random.randint(65, 90)) for _ in range(n))