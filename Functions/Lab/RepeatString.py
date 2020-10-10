word_string = input()
count_n = int(input())


def solve(word, count):
    result = ''
    for i in range(0, count):
        result += word
    return result


print(solve(word_string, count_n))
