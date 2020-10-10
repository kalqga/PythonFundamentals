product_type = input()
product_quantity = int(input())


def solve(p_type, p_quantity):
    total = None
    if p_type == 'coffee':
        total = p_quantity * 1.50
    elif p_type == 'water':
        total = p_quantity * 1.00
    elif p_type == 'coke':
        total = p_quantity * 1.40
    elif p_type == 'snacks':
        total = p_quantity * 2.00
    return f'{total:.2f}'


print(solve(product_type, product_quantity))
