string = input()

data = input().split()


def take(text):
    result = ''
    for index in range(0, len(text) + 1):
        if index == 0:
            result = result
        elif index % 2 == 0:
            result = result + text[index - 1]
    return result.lstrip()


def cut(text, start, end):
    start = int(start)
    end = int(end)
    arr = list(text)
    for i in range(end):
        arr.pop(start)
    return ''.join(arr)


def sub(text, first, second):
    text = text.replace(first, second)
    return text


while not data[0] == 'Done':

    if data[0] == 'TakeOdd':
        string = take(string)
        print(string)
    elif data[0] == 'Cut':
        string = cut(string, data[1], data[2])
        print(string)
    elif data[0] == 'Substitute':

        if data[1] in string:
            string = sub(string, data[1], data[2])
            print(string)
        else:
            print('Nothing to replace!')

    data = input().split()

print(f'Your password is: {string}')
