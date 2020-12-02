first_string, second_string = input().split()
total = 0

if len(first_string) == len(second_string):
    for i in range(len(first_string)):
        total += ord(first_string[i]) * ord(second_string[i])

elif len(first_string) > len(second_string):
    for i in range(len(second_string)):
        total += ord(first_string[i]) * ord(second_string[i])
    diff = (len(first_string) - len(second_string)) * -1
    for i in range(diff, 0):
        total += ord(first_string[i])

elif len(second_string) > len(first_string):
    for i in range(len(first_string)):
        total += ord(first_string[i]) * ord(second_string[i])
    diff = (len(second_string) - len(first_string)) * -1
    for i in range(diff, 0):
        total += ord(second_string[i])

print(total)
