n = int(input())
max_capacity = 255
capacity = 0

for i in range(1, n + 1):
    number = int(input())
    capacity += number
    if capacity > max_capacity:
        print('Insufficient capacity!')
        capacity -= number
print(capacity)
