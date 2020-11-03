price_data = input()
all_parts = 0
part_with_vat = 0
discount = 0.1
total = 0
tax = 0
all_taxes = 0


while True:

    if price_data == 'special' or price_data == 'regular':
        break
    if float(price_data) < 0:
        print('Invalid price!')
    else:

        tax = float(price_data) * 0.2
        part_with_vat = float(price_data) + tax
        all_parts += part_with_vat
        all_taxes += tax

    price_data = input()


if price_data == 'special':
    total = all_parts - (all_parts * discount)
    price_without_taxes = all_parts - all_taxes
    if total == 0:
        print('Invalid order!')
    else:
        print("Congratulations you've just bought a new computer!")
        print(f"Price without taxes: {price_without_taxes:.2f}$")
        print(f"Taxes: {all_taxes:.2f}$")
        print('-----------')
        print(f"Total price: {total:.2f}$")
elif price_data == 'regular':
    total = all_parts
    price_without_taxes = total - all_taxes
    if total == 0:
        print('Invalid order!')
    else:
        print("Congratulations you've just bought a new computer!")
        print(f"Price without taxes: {price_without_taxes:.2f}$")
        print(f"Taxes: {all_taxes:.2f}$")
        print('-----------')
        print(f"Total price: {total:.2f}$")
