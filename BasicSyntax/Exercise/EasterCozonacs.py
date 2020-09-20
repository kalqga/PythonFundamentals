budget = float(input())
flour_price = float(input())

eggs_price = flour_price * 0.75
milk_price = (flour_price + (flour_price * 0.25)) / 4

total_for_one_cozonac = flour_price + eggs_price + milk_price
eggs = 0
cozonac = 0

while budget > total_for_one_cozonac:
    budget -= total_for_one_cozonac
    cozonac += 1
    eggs += 3
    if cozonac % 3 == 0:
        eggs -= cozonac - 2

print(f'You made {cozonac} cozonacs! Now you have {eggs} eggs and {budget:.2f}BGN left.')
