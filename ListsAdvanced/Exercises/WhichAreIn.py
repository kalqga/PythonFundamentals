first_list = input().split(', ')
second_list = input().split(', ')
new_list = []

for substrings in first_list:

    for words in second_list:
        if substrings in words:
            if substrings in new_list:
                continue
            else:
                new_list.append(substrings)

print(new_list)
