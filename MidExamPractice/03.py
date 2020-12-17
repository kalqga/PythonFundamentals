string = input().split('@')

houses = [int(el) for el in string]

data = input().split()
start_index = 0

while not data[0] == "Love!":

    if data[0] == "Jump":
        jump_index = int(data[1])
        if jump_index + start_index >= len(houses):
            jump_index = 0
            start_index = 0
            if houses[jump_index] == 0:
                print(f"Place {jump_index} already had Valentine's day.")
            elif houses[jump_index] - 2 == 0:
                houses[jump_index] = 0
                print(f"Place {jump_index} has Valentine's day.")
            else:
                houses[jump_index] -= 2
        else:
            start_index += jump_index
            if houses[start_index] == 0:
                print(f"Place {start_index} already had Valentine's day.")
            elif houses[start_index] - 2 == 0:
                houses[start_index] = 0
                print(f"Place {start_index} has Valentine's day.")
            else:
                houses[start_index] -= 2

    data = input().split()

print(f"Cupid's last position was {start_index}.")

X = [i for i in houses if i != 0]

if len(X) > 0:
    print(f"Cupid has failed {len(X)} places.")
else:
    print(f"Mission was successful.")
