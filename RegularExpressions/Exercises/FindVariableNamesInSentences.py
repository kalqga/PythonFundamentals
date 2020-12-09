import re

data = input().split()
result = []

pattern = r'^[_][a-zA-Z]*[a-zA-Z]$'

for el in data:
    result += re.findall(pattern, el)

result = [el[1:] for el in result]

print(','.join(result))
