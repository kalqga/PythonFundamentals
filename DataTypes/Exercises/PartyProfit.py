import math

party_size = int(input())
days = int(input())
coins = 0
current_day = 0
current_party = party_size

for i in range(1, days + 1):
    if i % 10 == 0:
        current_party -= 2
    if i % 15 == 0:
        current_party += 5
    coins += 50 - (current_party * 2)
    if i % 3 == 0:
        coins -= current_party * 3
    if i % 5 == 0:
        coins += current_party * 20
        if i % 3 == 0:
            coins -= current_party * 2
print(f'{current_party} companions received {math.floor(coins / current_party)} coins each.')
