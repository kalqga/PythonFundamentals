product_prices = {}
product_quantities = {}
data = input()

while not data == 'buy':
    name, price, quantity = data.split()
    price = float(price)
    quantity = int(quantity)

    if name not in product_prices:
        product_prices[name] = price
        product_quantities[name] = quantity
    else:
        product_prices[name] = price
        product_quantities[name] += quantity
    data = input()


for key, value in product_prices.items():
    total_price = value * product_quantities[key]
    print(f'{key} -> {total_price:.2f}')

