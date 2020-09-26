import math

n = int(input())
p = int(input())

courses = math.floor(n / p)

if n % p == 0:
    print(courses)
else:
    result = courses + 1
    print(result)
