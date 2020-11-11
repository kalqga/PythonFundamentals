all_cards = input().split(':')

new_deck = []

data = input()


def add(card, deck):
    if card in all_cards:
        deck.append(card)
    else:
        print('Card not found.')


def insert(card, index, deck):
    if card in all_cards and 0 <= int(index) < len(deck):
        for i in range(0, len(deck)):
            if i == int(index):
                deck.insert(i, card)
    else:
        print('Error!')


def remove(card, deck):
    if card in deck:
        deck.remove(card)
    else:
        print('Card not found.')


def swap(card1, card2, deck):
    for index in range(0, len(deck)):
        if deck[index] == card1:
            deck.insert(index, card2)
            deck.pop(index + 1)
        elif deck[index] == card2:
            deck.insert(index, card1)
            deck.pop(index + 1)


while not data == "Ready":
    command = data.split()

    if command[0] == 'Add':
        add(command[1], new_deck)
    elif command[0] == 'Insert':
        insert(command[1], command[2], new_deck)
    elif command[0] == 'Remove':
        remove(command[1], new_deck)
    elif command[0] == 'Swap':
        swap(command[1], command[2], new_deck)
    elif data == 'Shuffle deck':
        new_deck.reverse()

    data = input()

print(' '.join(new_deck))
