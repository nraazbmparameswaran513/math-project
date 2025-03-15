import random
import sys

def get_random_code():
    num = random.randint(0, 10)
    if num % 2 == 0:
        return "print('The number is even')"
    else:
        return "print('The number is odd')"

get_random_code()