def asci(a, b):
    for i in range(ord(a) + 1, ord(b)):
        print(chr(i), end=' ')


asci(input(), input())
