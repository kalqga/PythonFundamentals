def exchange(nums_list, index):
    if 0 <= index < len(nums_list):
        first_part = nums_list[:index+1]
        second_part = nums_list[index+1:]
        exchanged_list = second_part + first_part
        return exchanged_list
    else:
        print("Invalid index")
        return nums_list


def get_max_odd(nums_list):
    filter_only_odds = filter(lambda x: x%2==1, nums_list)
    max_odd = max(filter_only_odds)

    for index in range(len(nums_list)-1, -1, -1):
        if nums_list[index] == max_odd:
            print(index)
            break


def get_max_even(nums_list):
    filter_only_evens = filter(lambda x: x%2==0, nums_list)
    max_even = max(filter_only_evens)

    for index in range(len(nums_list)-1, -1, -1):
        if nums_list[index] == max_even:
            print(index)
            break


numbers_as_string = input().split()

#list to int
numbers = list(map(int, numbers_as_string))

command = input()

while not command == "end":
    action, data = command.split()
    if action == 'exchange':
        result = exchange(numbers, int(data))
    elif command.split()[0] == 'max':
        if command.split()[1] == 'odd':
            get_max_odd(numbers)
        elif command.split()[1] == 'even':
            get_max_even(numbers)
    command = input()

