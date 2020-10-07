first_number = int(input())
second_number = int(input())

numbers = []

for i in range(1, (second_number * first_number) + 1):
    if i % first_number == 0:
        numbers.append(i)
print(numbers)
