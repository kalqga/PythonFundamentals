import re

data = input()
searched = input()

pattern = f"\\b{searched}\\b"

asd = re.findall(pattern, data, re.IGNORECASE)

print(len(asd))
