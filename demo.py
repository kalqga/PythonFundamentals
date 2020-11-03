people_waiting = int(input())
current_state = list(map(lambda x: int(x), input().split()))

###########################################

MAX_SEATS = 4

###########################################


for index in range(len(current_state)):
    while not current_state[index] == MAX_SEATS:
        if people_waiting > 0:
            current_state[index] += 1
            people_waiting -= 1
        else:
            break

all_seats = len(current_state) * MAX_SEATS
taken = sum(current_state)

if people_waiting == 0 and taken < all_seats:
    print("The lift has empty spots!")
elif people_waiting > 0 and taken == all_seats:
    print(f"There isn't enough space! {people_waiting} people in a queue!")
print(' '.join(str(x) for x in current_state))
