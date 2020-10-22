# Fire Range

RANGE_HIGH = range(81, 126)
RANGE_MEDIUM = range(51, 81)
RANGE_LOW = range(1, 51)

#############################################

# Input

text = input()
water = int(input())

##############################################

# Body

total_water = water
fire_data = text.split('#')
effort = 0
put_out_fire = []


################################################

for fire in fire_data:
    type_of_fire, value = fire.split(' = ')
    value = int(value)

    if type_of_fire == 'High' and value not in RANGE_HIGH:
        continue
    elif type_of_fire == 'Medium' and value not in RANGE_MEDIUM:
        continue
    elif type_of_fire == 'Low' and value not in RANGE_LOW:
        continue

    if total_water >= value:
        total_water -= value
        effort += (value * 0.25)
        put_out_fire.append(value)

##################################################

# PRINT

print('Cells:')
for i in put_out_fire:
    print(f' - {i}')

print(f'Effort: {effort:.2f}')
print(f'Total Fire: {sum(put_out_fire)}')

