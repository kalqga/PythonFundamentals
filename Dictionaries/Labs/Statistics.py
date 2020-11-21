
product_stash = {}
data = input()

while not data == 'statistics':

    command = data.split(': ')

    key = command[0]
    value = command[1]

    if key in product_stash.keys():
        product_stash[key] += int(value)
    else:
        product_stash[key] = int(value)

    data = input()

print("Products in stock:")
for key, value in product_stash.items():
    print(f"- {key}: {value}")
print(f"Total Products: {len(product_stash)}")
print(f"Total Quantity: {sum(product_stash.values())}")
