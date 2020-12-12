n = int(input())

pieces = {}

for i in range(n):
    data = input().split('|')
    pieces[data[0]] = [data[1], data[2]]

command = input().split('|')


def add(piece, composer, key, dic):
    if piece in dic.keys():
        return f"{piece} is already in the collection!"
    else:
        dic[piece] = [composer, key]
        return f"{piece} by {composer} in {key} added to the collection!"


def remove(piece, dic):
    if piece in dic.keys():
        dic.pop(piece)
        return f"Successfully removed {piece}!"
    else:
        return f"Invalid operation! {piece} does not exist in the collection."


def change(piece, new_key, dic):
    if piece in dic.keys():
        dic[piece] = [dic[piece][0], new_key]
        return f"Changed the key of {piece} to {new_key}!"
    else:
        return f"Invalid operation! {piece} does not exist in the collection."


while not command[0] == 'Stop':

    if command[0] == 'Add':
        print(add(command[1], command[2], command[3], pieces))
    elif command[0] == 'Remove':
        print(remove(command[1], pieces))
    elif command[0] == 'ChangeKey':
        print(change(command[1], command[2], pieces))

    command = input().split('|')

a = dict(sorted(pieces.items(), key=lambda x: x[0]))

for key, value in a.items():
    print(f"{key} -> Composer: {value[0]}, Key: {value[1]}")
