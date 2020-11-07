import math

budget = float(input())
students = int(input())
price_of_flour = float(input())
price_of_egg = float(input())
price_of_apron = float(input())

free_flour = 0
flours = 0
total_flour = 0
eggs = 0
total_eggs = 0
aprons = 0
total_aprons = 0

for student in range(0, students):
    eggs += 1
    flours += 1
    if flours % 5 == 0:
        free_flour += 1

total_flour = (flours - free_flour) * price_of_flour
total_eggs = eggs * (price_of_egg * 10)
total_aprons = (students + math.ceil(students * 0.2)) * price_of_apron

total_price = total_aprons + total_eggs + total_flour

if total_price <= budget:
    print(f"Items purchased for {total_price:.2f}$.")
else:
    print(f"{math.fabs(budget - total_price):.2f}$ more needed.")
