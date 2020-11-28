data = input()
digits = ''
chars = ''
other = ''
for el in data:
    if el.isdigit():
        digits += el
    elif el.isalpha():
        chars += el
    else:
        other += el
print(digits)
print(chars)
print(other)
