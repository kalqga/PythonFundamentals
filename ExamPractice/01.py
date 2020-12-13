email = input()

data = input().split()


def upper(mail):
    mail = mail.upper()
    return mail


def lower(mail):
    mail = mail.lower()
    return mail


def domain(mail, count):
    arr = []
    count = int(count)
    for i in range(len(mail) - count, len(mail)):
        arr.append(mail[i])
    return ''.join(arr)


def username(mail):
    arr = []
    if '@' in mail:
        for el in mail:
            if el == '@':
                break
            else:
                arr.append(el)
        return ''.join(arr)
    else:
        return f"The email {mail} doesn't contain the @ symbol."


def replace(mail, char):
    mail = mail.replace(char, '-')
    return mail


while not data[0] == 'Complete':

    if data[0] == "Make" and data[1] == "Upper":
        email = upper(email)
        print(email)
    elif data[0] == "Make" and data[1] == "Lower":
        email = lower(email)
        print(email)
    elif data[0] == "GetDomain":
        print(domain(email, data[1]))
    elif data[0] == "GetUsername":
        print(username(email))
    elif data[0] == "Replace":
        email = replace(email, data[1])
        print(email)
    elif data[0] == "Encrypt":
        for el in email:
            print(ord(el), end=' ')

    data = input().split()
