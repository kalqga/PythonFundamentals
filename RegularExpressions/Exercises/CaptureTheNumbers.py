import re

data = input()
empt = []

pattern = r'\d+'

while data:

    a = re.findall(pattern, data)
    empt.extend(a)
    data = input()

print(*empt, sep=' ')
