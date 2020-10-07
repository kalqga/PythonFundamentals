string = input()
shuffle = int(input())

cards = string.split(' ')

first = cards[0]
last = cards[len(cards) - 1]

cards.pop(0)
cards.pop(len(cards) - 1)

for i in range(shuffle):
    list_left = cards[:len(cards) // 2]
    list_right = cards[len(cards) // 2:]
    cards = []
    for index in range(len(list_left)):
        cards.append(list_right[index])
        cards.append(list_left[index])

cards.append(last)
cards.insert(0, first)

print(cards)
