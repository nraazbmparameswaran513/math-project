import random
def get_random_code(length):
    code = ''
    for i in range(length):
        code += str(random.randint(0, 9))
    return code