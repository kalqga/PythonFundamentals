data = input().split()
result = ''

for i in data:
    length = len(i)
    result += i * length

print(result)
