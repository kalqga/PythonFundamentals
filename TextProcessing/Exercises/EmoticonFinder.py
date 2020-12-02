data = input()

index = 0

while index < len(data):

    if data[index] == ':':
        print(f':{data[index+1]}')
    index += 1
