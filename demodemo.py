num = int(input())
wagons = [0 for _ in range(num)]

command = input()

while not command == 'End':

    data = command.split()

    if data[0] == 'add':
        number_of_people = int(data[1])
        wagons[-1] += number_of_people
    elif data[0] == 'insert':
        index = int(data[1])
        value = int(data[2])
        wagons[index] += value

    elif data[0] == 'leave':
        index = int(data[1])
        value = int(data[2])
        wagons[index] -= value

    command = input()


print(wagons)
