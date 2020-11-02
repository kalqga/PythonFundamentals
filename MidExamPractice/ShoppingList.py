initial_list = input().split('!')
data = input()


def add_data(item):
    if item in initial_list:
        pass
    else:
        initial_list.insert(0, item)


def remove_data(item):
    if item in initial_list:
        initial_list.remove(item)


def change_data(old_item, new_item):
    if old_item in initial_list:
        for index in range(0, len(initial_list)):
            if initial_list[index] == old_item:
                initial_list.insert(index, new_item)
                initial_list.pop(index + 1)
            else:
                continue


def add_remove(item):
    if item in initial_list:
        initial_list.remove(item)
        initial_list.append(item)


while not data == 'Go Shopping!':

    command = data.split()

    if command[0] == 'Urgent':
        add_data(command[1])
    elif command[0] == 'Unnecessary':
        remove_data(command[1])
    elif command[0] == 'Correct':
        change_data(command[1], command[2])
    elif command[0] == 'Rearrange':
        add_remove(command[1])

    data = input()


print(', '.join(initial_list))
