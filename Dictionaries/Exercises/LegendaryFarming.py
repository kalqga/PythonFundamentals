key_materials = {'shards': 0, 'fragments': 0, 'motes': 0}
junk = {}
asd = True

while asd:
    data = input().split()
    for i in range(0, len(data), 2):
        value = int(data[i])
        key = data[i + 1].lower()

        if key in key_materials.keys():
            key_materials[key] += value
            if key_materials[key] >= 250:
                if key == 'shards':
                    print('Shadowmourne obtained!')
                elif key == 'fragments':
                    print('Valanyr obtained!')
                elif key == 'motes':
                    print('Dragonwrath obtained!')
                key_materials[key] -= 250
                asd = False
                break
        else:
            if key in junk.keys():
                junk[key] += value
            else:
                junk[key] = value

sorted_materials = sorted(key_materials.items(), key=lambda x: (-x[1], x[0]))
sorted_junk = sorted(junk.items(), key=lambda x: x[0])

for key, value in sorted_materials:
    print(f'{key}: {value}')
for key, value in sorted_junk:
    print(f'{key}: {value}')
