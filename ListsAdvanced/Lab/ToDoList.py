notes = ['asd' for _ in range(10)]

command = input()

while not command == 'End':

    data = command.split('-')
    index = int(data[0])
    string = data[1]
    notes.remove('asd')
    notes.insert(index, string)

    command = input()

result = []

for el in notes:
    if el != 'asd':
        result.append(el)
print(result)
