import re
data = input()
pattern = "\\b[A-Z][a-z]+\s[A-Z][a-z]+"

names = re.findall(pattern, data)
print(' '.join(names))
