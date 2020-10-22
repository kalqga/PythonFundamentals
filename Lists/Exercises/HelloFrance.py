# INPUT

collection_of_items = input().split('|')
budget = float(input())

####################################################

# VARIABLES

new_prices = []
profit = 0.0

####################################################

# MAIN BODY

for item in collection_of_items:
    type_of_item, price = item.split('->')
    price = float(price)

    if type_of_item == 'Clothes' and price > 50.00:
        continue
    elif type_of_item == 'Shoes' and price > 35.00:
        continue
    elif type_of_item == 'Accessories' and price > 20.50:
        continue

    if budget >= price:
        budget -= price
        new = price * 0.4
        profit += new
        new_prices.append(price + new)

#################################################################

# PRINT

for el in new_prices:
    print(f'{el:.2f}', end=' ')

print()
print(f'Profit: {profit:.2f}')

if (sum(new_prices) + budget) >= 150:
    print('Hello, France!')
else:
    print('Time to go.')

