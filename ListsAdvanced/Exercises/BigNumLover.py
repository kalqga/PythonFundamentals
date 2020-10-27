string = input().split()

string.sort(reverse=True)

for el in string:
    print("".join(el), end='')

