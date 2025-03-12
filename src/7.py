import random
def get_random_code():
    code = "".join(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ") for _ in range(10))
    return code