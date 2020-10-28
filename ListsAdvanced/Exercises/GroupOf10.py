numbers = list(map(int, input().split(', ')))

num_range = 10

while len(numbers) > 0:
    list1 = [el for el in numbers if el <= num_range]
    print(f"Group of {num_range}'s: {list1}")

    for el in list1:
        numbers.remove(el)
    num_range += 10
    list1 = []
