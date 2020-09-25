n = int(input())

for i in range(0, n):
    i += 1
    if sum(map(int, str(i))) == 5 or sum(map(int, str(i))) == 7 or sum(map(int, str(i))) == 11:
        print(f'{i} -> True')
    else:
        print(f'{i} -> False')
