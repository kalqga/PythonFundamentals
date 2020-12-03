data = input()
index = 0

while index < len(data):
    if index == (len(data) - 1):
        break
    elif data[index] == data[index + 1]:
        data = data.replace(data[index+1], '', 1)
        if index != 0:
            index -= 1
    else:
        index += 1

print(data)







# aaaaabbbbbcdddeeeedssaa
# qqqwerqwecccwd