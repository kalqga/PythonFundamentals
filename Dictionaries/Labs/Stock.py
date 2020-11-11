elements = input().split()
to_search = input(). split()
bakery = {}

for index in range(0, len(elements), 2):
    key = elements[index]
    value = elements[index + 1]
    bakery[key] = int(value)

for el in to_search:
    if el in bakery:
        print(f"We have {bakery[el]} of {el} left")
    else:
        print(f"Sorry, we don't have {el}")
