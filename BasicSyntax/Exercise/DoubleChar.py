word = input()


def multichar(word, n):
    return ''.join([x * n for x in word])
