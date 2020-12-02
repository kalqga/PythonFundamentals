data = input()
character = 0
new_text = ''
for i in range(0, len(data)):
    character = ord(data[i]) + 3
    new_text += chr(character)

print(new_text)
