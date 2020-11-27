courses = {}
data = input()
while not data == 'end':
    course, name = data.split(' : ')

    if course not in courses:
        courses[course] = []
        courses[course].append(name)
    else:
        courses[course].append(name)

    data = input()

for key, value in sorted(courses.items(), key=lambda x: -len(x[1])):
    print(f"{key}: {len(value)}")
    for person in sorted(courses[key]):
        print(f"-- {person}")
