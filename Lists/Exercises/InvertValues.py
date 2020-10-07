string = input()

list1 = string.split(' ')

for i in range(len(list1)):
    if not int(list1[i]) == 0:
        list1[i] = -int(list1[i])
    else:
        list1[i] = int(list1[i])

print(list1)
