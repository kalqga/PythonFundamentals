initial_loot = input().split('|')
##############################################
new_loot = initial_loot.copy()
data = input()
stolen_loot = []


##############################################


def loot(command_list, other_list):
    for item in range(1, len(command_list)):
        if command_list[item] in other_list:
            pass
        else:
            other_list.insert(0, command_list[item])


def drop(command_list, other_list):
    index = int(command_list[1])
    if 0 <= index < len(other_list):
        other_list.append(other_list[index])
        other_list.pop(index)
    else:
        pass


while data != 'Yohoho!':
    command = data.split()

    if command[0] == 'Loot':
        loot(command, new_loot)

    elif command[0] == 'Drop':
        drop(command, new_loot)

    elif command[0] == 'Steal':
        index = int(command[1])
        if index >= len(new_loot):
            stolen_loot = new_loot.copy()
            new_loot.clear()
            print(', '.join(stolen_loot))
        elif index < 0:
            pass
        else:
            for i in range(len(new_loot) - index, len(new_loot)):
                stolen_loot.append(new_loot[i])
            for i in range(len(new_loot), len(new_loot) - index, -1):
                new_loot.pop()
            print(', '.join(stolen_loot))

    data = input()

asd = 0

for word in new_loot:
    asd += len(word)

if len(new_loot) > 0:
    print(f"Average treasure gain: {asd / len(new_loot):.2f} pirate credits.")
else:
    print("Failed treasure hunt.")
