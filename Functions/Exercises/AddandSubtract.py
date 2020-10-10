first_num = int(input())
second_num = int(input())
third_num = int(input())


def add_and_subtract(f, s, t):
    sum_numbers(f, s)
    return subtract(f, s, t)


def sum_numbers(c, d):
    sum_result = c + d
    return sum_result


def subtract(a, b, c):
    result1 = sum_numbers(a, b)
    result = result1 - c
    print(result)


add_and_subtract(first_num, second_num, third_num)
