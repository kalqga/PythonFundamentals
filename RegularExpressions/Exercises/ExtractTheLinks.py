import re

pattern = r">>(?P<name>[A-Za-z]+)<<(?P<price>\d+(?P<no>.\d+)?)!(?P<quantity>\d+)"

data = input()
date = ''
suma = 0

while not data == 'Purchase':
    if re.search(pattern, data):
        date += ' ' + data
    data = input()

a = re.finditer(pattern, date)
print(f"Bought furniture:")
for el in a:
    dic = el.groupdict()
    print(dic['name'])
    suma += float(dic['price']) * int(dic['quantity'])
print(f"Total money spend: {suma:.2f}")
