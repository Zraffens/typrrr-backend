from random import randint


def code_generator() -> int:
    random = [str(randint(0, 9)) for index in range(5)]
    return int(''.join(random))
