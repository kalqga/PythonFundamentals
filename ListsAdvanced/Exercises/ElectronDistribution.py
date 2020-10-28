total_electrons = int(input())

distribution = []
index = 0

while total_electrons >= 0:

    max_electrons = 2 * (index + 1) ** 2

    if max_electrons <= total_electrons:
        distribution.append(max_electrons)
    else:
        if total_electrons <= 0:
            break
        else:
            distribution.append(total_electrons)
            break
    total_electrons -= max_electrons
    index += 1

print(distribution)
