import string


def lnd(string2):
    if not string2.isalnum():
        print("Password must consist only of letters and digits")
        digitt(string2)
    else:
        digitt(string2)


def between(string1):
    if not 6 <= len(string1) <= 10:
        print("Password must be between 6 and 10 characters")
        lnd(string1)
    else:
        lnd(string1)


def digitt(string3):
    number = False
    digit_count = 0
    for i in string3:
        if i.isdigit():
            number = True
            digit_count += 1
    if digit_count < 2:
        print("Password must have at least 2 digits")
    else:
        print("Password is valid")


between(input())
