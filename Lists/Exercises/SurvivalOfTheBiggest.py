nums = input()
n = int(input())

numbers = nums.split()
nu = 0

arr = []

for el in numbers:
    a = int(el)
    arr.append(a)

while nu < n:
    arr.remove(min(arr))

    nu += 1

print(arr)
