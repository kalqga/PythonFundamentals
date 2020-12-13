import re

pattern = r"(?P<user>[U]\$)(?P<username>[A-Z][a-z][a-z]+)(?P=user)(?P<pass>[P]\@\$)(?P<password>[A-Za-z]{4}[A-Za-z]+\d+)(?P=pass)"

n = int(input())
count = 0
dic = {}

for i in range(0, n):
    data = input()

    a = re.findall(pattern, data)
    if a:
        print("Registration was successful")
        for el in a:
            print(f"Username: {el[1]}, Password: {el[3]}")
        count += 1
    else:
        print("Invalid username or password")

print(f"Successful registrations: {count}")
