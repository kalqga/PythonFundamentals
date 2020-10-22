string = input()

arr = string.split()
arr2 = []
for el in arr:
    res = int(el) * -1
    arr2.append(res)

print(arr2)
