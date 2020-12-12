import re

times = int(input())
pattern = r'@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+'


def sss(dsa):
    arr = []
    for el in dsa:
        for ind in el:
            if ind.isdigit():
                arr.append(ind)
    if len(arr) == 0:
        return 'Product group: 00'
    else:
        return f"Product group: {''.join(arr)}"


for i in range(0, times):

    data = input()

    asd = re.findall(pattern, data)
    if asd:
        print(sss(asd))
    else:
        print('Invalid barcode')
