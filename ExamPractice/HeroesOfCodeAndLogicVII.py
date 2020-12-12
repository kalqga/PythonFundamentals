chars_to_choose = int(input())

characters = {}

for i in range(chars_to_choose):
    name, HP, MP = input().split()
    characters[name] = [int(HP), int(MP)]

data = input().split(' - ')


def spell(hero_name, mp_needed, spell_name, chars):
    for hero, current_mp in chars.items():
        if hero == hero_name:
            if current_mp[1] >= int(mp_needed):
                current_mp[1] -= int(mp_needed)
                return f"{hero} has successfully cast {spell_name} and now has {current_mp[1]} MP!"
            else:
                return f"{hero} does not have enough MP to cast {spell_name}!"


def dmg(hero_name, damage, attacker, chars):
    for hero, hp in chars.items():
        if hero == hero_name:
            if hp[0] > int(damage):
                hp[0] -= int(damage)
                return f"{hero} was hit for {damage} HP by {attacker} and now has {hp[0]} HP left!"
            else:
                chars.pop(hero)
                return f"{hero} has been killed by {attacker}!"


def recharge(hero_name, amount, chars):
    for hero, mana in chars.items():
        if hero == hero_name:
            man = int(amount) + mana[1]
            if man < 200:
                mana[1] += int(amount)
                return f"{hero} recharged for {amount} MP!"
            elif man >= 200:
                m = mana[1]
                mana[1] = 200
                return f"{hero} recharged for {200 - m} MP!"


def heal(hero_name, amount, chars):
    for hero, hp in chars.items():
        if hero == hero_name:
            health = int(amount) + hp[0]
            if health < 100:
                hp[0] += int(amount)
                return f"{hero} healed for {amount} HP!"
            elif health >= 100:
                hl = hp[0]
                hp[0] = 100
                return f"{hero} healed for {100 - hl} HP!"


while not data[0] == 'End':

    if data[0] == 'CastSpell':
        print(spell(data[1], data[2], data[3], characters))
    elif data[0] == 'TakeDamage':
        print(dmg(data[1], data[2], data[3], characters))
    elif data[0] == 'Recharge':
        print(recharge(data[1], data[2], characters))
    elif data[0] == 'Heal':
        print(heal(data[1], data[2], characters))

    data = input().split(' - ')

a = dict(sorted(characters.items(), key=lambda x: (-x[1][0], x[0])))

for key, value in a.items():
    print(key)
    print(f"  HP: {value[0]}")
    print(f"  MP: {value[1]}")
