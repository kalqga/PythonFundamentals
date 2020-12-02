data = input().split(', ')
asd = True
for username in data:
    asd = True
    if 3 <= len(username) <= 16:
        for el in username:
            if el.isalpha():
                continue
            elif el.isdigit():
                continue
            elif el == '-':
                continue
            elif el == '_':
                continue
            else:
                asd = False
                break
        if asd:
            print(username)
