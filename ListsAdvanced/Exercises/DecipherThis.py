message = input().split()


for el in message:
    numbers = []
    letters = []
    for element in el:
        if element.isdigit():
            numbers.append(element)
        else:
            letters.append(element)

    character = int(''.join(numbers))
    asd = chr(character)

    letters[0], letters[-1] = letters[-1], letters[0]

    print(f"{asd}{''.join(letters)}", end=' ')
