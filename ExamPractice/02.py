users = {}

command = input().split('->')


while not command[0] == 'Statistics':

    if command[0] == "Add":
        if command[1] in users:
            print(f"{command[1]} is already registered")
        else:
            users[command[1]] = []
    elif command[0] == "Send":
        users[command[1]].append(command[2])
    elif command[0] == "Delete":
        if command[1] in users:
            users.pop(command[1])
        else:
            print(f"{command[1]} not found!")

    command = input().split('->')

print(f"Users count: {len(users)}")


a = dict(sorted(users.items(), key=lambda x: (-len(x[1]), x[0])))


for key, value in a.items():
    print(key)
    for el in value:
        print(f" - {el}")

