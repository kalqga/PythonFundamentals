n = int(input())

wagon = []

for i in range(0, n):
    wagon.append(int(0))


string = input()
while string != 'End':
    string = input()
    command = string.split(' ')

    if command[0] == 'add':
        wagon.remove(wagon[n])
        wagon.append(command[1])

print(wagon)