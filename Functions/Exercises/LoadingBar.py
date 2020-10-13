def loading(number):
    perc = int(number / 10) * '%'
    dots = int((100 - number) / 10) * '.'
    if number <= 90:
        print(f'{number}% [{perc}{dots}]')
        print('Still loading...')
    else:
        print(f'100% Complete!')
        print(f'[{perc}]')


loading(int(input()))
