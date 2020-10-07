import sys

string = input()
n = int(input())

numbers = string.split(' ')


for i in range(n):
    min_num = sys.maxsize
    for ind in numbers:
        if int(ind) < min_num:
            min_num = int(ind)
    numbers.remove(str(min_num))

sec = []
for ind in numbers:
    sec.append(int(ind))

print(sec)
