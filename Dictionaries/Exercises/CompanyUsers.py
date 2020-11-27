companies = {}

data = input()

while not data == 'End':

    name, identification = data.split(' -> ')

    if name not in companies:
        companies[name] = []
        companies[name].append(identification)
    else:
        if identification not in companies[name]:
            companies[name].append(identification)

    data = input()

for key, value in sorted(companies.items(), key=lambda x: x[0]):
    print(key)
    for ids in value:
        print(f"-- {ids}")
