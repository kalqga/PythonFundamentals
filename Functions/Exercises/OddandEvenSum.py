def even_and_odd(string):
    sum_even = 0
    sum_odd = 0
    for i in string:
        if int(i) % 2 == 0:
            sum_even += int(i)
        else:
            sum_odd += int(i)
    print(f'Odd sum = {sum_odd}, Even sum = {sum_even}')


even_and_odd(input())
