def palindrome(string):
    arr = string.split(', ')
    for i in arr:
        arr2 = list(i)
        arr3 = list(i)
        arr3.reverse()
        if arr2 == arr3:
            print(True)
        else:
            print(False)


palindrome(input())
