def chars(char1, char2):
    first = ord(char1)
    last = ord(char2)
    for i in range(first + 1, last):
        print(chr(i), end=' ')


chars(input(), input())
