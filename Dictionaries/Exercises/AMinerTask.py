data = input()
count = 1
dictionary = {}

while not data == 'stop':

    if count % 2 == 0:
        value = int(data)
        dictionary[key] += value
    else:
        key = data
        if key in dictionary.keys():
            pass
        else:
            dictionary[key] = 0

    count += 1
    data = input()

for key, value in dictionary.items():
    print(f"{key} -> {value}")

