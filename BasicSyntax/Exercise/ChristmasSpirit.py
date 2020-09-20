quantity = int(input())
days = int(input())
total_money = 0
spirit = 0

for day in range(1, days + 1):
    if day % 11 == 0:
        quantity += 2
    if day % 2 == 0:
        total_money += 2 * quantity
        spirit += 5
    if day % 3 == 0:
        total_money += (quantity * 5) + (quantity * 3)
        spirit += 13
    if day % 5 == 0:
        total_money += quantity * 15
        spirit += 17
        if day % 3 == 0:
            spirit += 30
    if day % 10 == 0:
        spirit -= 20
        total_money += 5 + 3 + 15
        if day == days:
            spirit -= 30

print(f'Total cost: {total_money}')
print(f'Total spirit: {spirit}')
