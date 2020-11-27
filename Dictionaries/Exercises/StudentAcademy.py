n = int(input())
students = {}
avg_students = {}
for i in range(0, n):
    name = input()
    grade = float(input())

    if name not in students:
        students[name] = []
        students[name].append(grade)
    else:
        students[name].append(grade)

for key, value in students.items():
    avg_students[key] = sum(value)/len(value)

for key, value in sorted(avg_students.items(), key=lambda x: -x[1]):
    if value >= 4.50:
        print(f"{key} -> {value:.2f}")

