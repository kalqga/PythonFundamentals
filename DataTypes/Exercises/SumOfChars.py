n = int(input())
result = 0

for i in range(0, n):
    i = input()
    result += ord(i)

print(f'The sum equals: {result}')
