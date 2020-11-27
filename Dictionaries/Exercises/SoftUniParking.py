n = int(input())
registered_users = {}

for i in range(0, n):
    data = input().split()

    if data[0] == 'register':
        if data[1] not in registered_users.keys():
            registered_users[data[1]] = data[2]
            print(f'{data[1]} registered {data[2]} successfully')
        else:
            print(f'ERROR: already registered with plate number {data[2]}')
    elif data[0] == 'unregister':
        if data[1] not in registered_users.keys():
            print(f'ERROR: user {data[1]} not found')
        else:
            registered_users.pop(data[1])
            print(f"{data[1]} unregistered successfully")

for user, licence in registered_users.items():
    print(f"{user} => {licence}")
