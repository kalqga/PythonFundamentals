numbers = list(map(lambda x: int(x), input().split()))

data = input()


def Shoot(nums, i, v):
    if i in range(len(nums)):
        nums[i] -= v
        if nums[i] <= 0:
            nums.pop(i)
    return nums


def Add(nums, i, v):
    if i in range(len(nums)):
        nums.insert(i, v)
    else:
        print('Invalid placement!')
    return nums


def Strike(nums, i, v):
    back_index = i - v
    front_index = v + i

    if back_index in range(len(nums)) and front_index in range(len(nums)):
        for ind in range(back_index, front_index + 1):
            nums.pop(back_index)
    else:
        print('Strike missed!')
    return nums


while not data == 'End':

    command, index, value = data.split()
    index = int(index)
    value = int(value)

    if command == 'Shoot':
        Shoot(numbers, index, value)
    elif command == 'Add':
        Add(numbers, index, value)
    elif command == 'Strike':
        Strike(numbers, index, value)

    data = input()

string = list(map(lambda x: str(x), numbers))

print('|'.join(string))
