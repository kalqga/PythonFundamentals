def perfect(number):
    total = 0
    for i in range(1, number + 1):
        if number % i == 0:
            total += i
            if total == number:
                return 'We have a perfect number!'
            elif total > number:
                return "It's not so perfect."
        else:
            continue


print(perfect(int(input())))
