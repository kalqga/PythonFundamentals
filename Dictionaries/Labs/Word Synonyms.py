n = int(input())
dictionary = {}

for i in range(0, n):
    first_word = input()
    second_word = input()
    if first_word in dictionary.keys():
        dictionary[first_word] += (', ' + second_word)
    else:
        dictionary[first_word] = second_word


for key, value in dictionary.items():
    print(f"{key} - {value}")

