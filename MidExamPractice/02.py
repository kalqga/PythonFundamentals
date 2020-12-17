def include(coffee, cof_list):
    cof_list.append(coffee)
    return cof_list


def remove_first(number, cof_list):
    number = int(number)
    for el in range(number):
        cof_list.pop(0)
    return cof_list


def remove_last(number, cof_list):
    number = int(number)
    if len(cof_list) <= number:
        return cof_list
    else:
        for el in range(number):
            cof_list.pop(-1)
        return cof_list


def prefer(coffee1, coffee2, cof_list):
    coffee1 = int(coffee1)
    coffee2 = int(coffee2)
    if coffee1 < len(cof_list) and coffee2 < len(cof_list):
        cof_list[coffee1], cof_list[coffee2] = cof_list[coffee2], cof_list[coffee1]
        return cof_list
    else:
        return cof_list


starting_list = input().split()
num_of_commands = int(input())

for i in range(num_of_commands):

    data = input().split()

    if data[0] == "Include":
        starting_list = include(data[1], starting_list)
    elif data[0] == "Remove":
        if data[1] == 'first':
            starting_list = remove_first(data[2], starting_list)
        elif data[1] == 'last':
            starting_list = remove_last(data[2], starting_list)
    elif data[0] == "Prefer":
        starting_list = prefer(data[1], data[2], starting_list)
    elif data[0] == "Reverse":
        starting_list.reverse()

print("Coffees:")
print(' '.join(starting_list))
