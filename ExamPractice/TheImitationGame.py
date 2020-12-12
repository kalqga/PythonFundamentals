message = input()

command = input().split('|')


def move(num, msg):
    arr = []
    for index in range(0, int(num)):
        arr.append(msg[index])
    msg = msg[int(num):len(msg)]
    msg = msg + ''.join(arr)
    return msg


def insert(index, value, msg):
    index = int(index)
    return msg[:index] + value + msg[index:]


def change(substring, replacement, msg):
    msg = msg.replace(substring, replacement)
    return msg


while not command[0] == 'Decode':

    if command[0] == 'Move':
        message = move(command[1], message)
    elif command[0] == 'Insert':
        message = insert(command[1], command[2], message)
    elif command[0] == 'ChangeAll':
        message = change(command[1], command[2], message)

    command = input().split('|')

print(f"The decrypted message is: {message}")
