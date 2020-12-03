import re
data = input()
pattern = "(\+359-2-[0-9]{3}-[0-9]{4}|\+359 2 [0-9]{3} [0-9]{4})\\b"

number = re.findall(pattern, data)

print(', '.join(number))
