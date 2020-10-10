first_num = int(input())
second_num = int(input())
third_num = int(input())


def solve(a, b, c):
    if a > c and b > c:
        return c
    elif a > b and c > b:
        return b
    elif b > a and c > a:
        return a


print(solve(first_num, second_num, third_num))
