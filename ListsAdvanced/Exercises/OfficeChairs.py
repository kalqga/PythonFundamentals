rooms = int(input())

count = 0
free_chairs = 0
needed_chairs = 0
asd = False

while count < rooms:
    count += 1

    data = input().split()
    chairs = int(len(data[0]))
    people = int(data[1])

    if people > chairs:
        needed_chairs = people - chairs
        print(f'{needed_chairs} more chairs needed in room {count}')
        asd = True
    else:
        free_chairs += chairs - people

if asd:
    pass
else:
    print(f'Game On, {free_chairs} free chairs left')
