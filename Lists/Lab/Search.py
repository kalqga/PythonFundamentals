n = int(input())
word = input()

arr = []
fil = []

for i in range(n):
    text = input()
    arr.append(text)
    if word in text:
        fil.append(text)

print(arr)
print(fil)
