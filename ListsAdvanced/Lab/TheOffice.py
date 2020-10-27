employee_happiness = input().split()
factor = int(input())

new_employees = list(map(lambda x: int(x) * factor, employee_happiness))

filtered_employees = list(filter(lambda x: x >= (sum(new_employees) / len(new_employees)), new_employees))

if len(filtered_employees) / len(new_employees) >= 0.5:
    print(f'Score: {len(filtered_employees)}/{len(employee_happiness)}. Employees are happy!')
else:
    print(f'Score: {len(filtered_employees)}/{len(employee_happiness)}. Employees are not happy!')
