first = int(input())
second = int(input())
third = int(input())


def sum_numbers(a, b):
    result = a + b
    return result


def subtract(a, b):
    result = a - b
    return result


def add_and_subtract(a, b, c):
    return subtract(sum_numbers(a, b), c)


print(add_and_subtract(first, second, third))
