text = input()
shuffles = int(input())
cards = text.split()

n = 0
top_card = cards[0]
bottom_card = cards[-1]
cards.pop(0)
cards.pop(-1)

middle = len(cards) // 2

while n < shuffles:

    right = []
    left = []
    shuffled_list = []

    for index in range(0, middle):
        left.append(cards[index])

    for index in range(middle, len(cards)):
        right.append(cards[index])

    for i in range(0, middle):
        shuffled_list.append(right[i])
        shuffled_list.append(left[i])

    cards = shuffled_list.copy()

    n += 1

arr = cards.copy()
arr.insert(0, top_card)
arr.insert(len(arr), bottom_card)

print(arr)
