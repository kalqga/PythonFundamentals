lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

count_helmet = 0
count_sword = 0
count_shield = 0
count_armor = 0

for i in range(1, lost_fights + 1):
    if i % 2 == 0:
        count_helmet += 1
    if i % 3 == 0:
        count_sword += 1
        if i % 2 == 0:
            count_shield += 1
            if count_shield % 2 == 0:
                count_armor += 1


helmet = helmet_price * count_helmet
sword = sword_price * count_sword
shield = shield_price * count_shield
armor = armor_price * count_armor
total = helmet + sword + shield + armor

print(f'Gladiator expenses: {total:.2f} aureus')
