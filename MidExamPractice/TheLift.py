people_waiting = int(input())
current_state = list(map(lambda x: int(x), input().split()))

###########################################

queue = people_waiting
to_add = 0
new_value = 0

###########################################


for index in range(0, len(current_state)):
    if queue >= 4:
        if current_state[index] < 4:
            to_add = 4 - current_state[index]
            new_value = current_state[index] + to_add
            current_state.insert(index, new_value)
            current_state.pop(index+1)
            queue -= to_add
        else:
            pass
    else:
        to_add = queue
        current_state.insert(index, to_add)
        current_state.pop(index+1)

if sum(current_state) < people_waiting:
    if queue <= 0:
        print(' '.join(str(x) for x in current_state))
    else:
        print(f"There isn't enough space! {queue} people in a queue!")
        print(' '.join(str(x) for x in current_state))

else:
    if queue <= 0:
        print(''.join(current_state))
    else:
        print("The lift has empty spots!")
        print(' '.join(str(x) for x in current_state))
