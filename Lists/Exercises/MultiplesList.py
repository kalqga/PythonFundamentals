factor = int(input())
count = int(input())

arr = [el for el in range(factor, factor * count + 1, factor)]

print(arr)
