import math


def division(num_1, num_2):
    first = math.factorial(num_1)
    second = math.factorial(num_2)
    divide = first / second
    print(f'{divide:.2f}')


division(int(input()), int(input()))
