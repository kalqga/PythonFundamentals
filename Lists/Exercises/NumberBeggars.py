string = input()
beggars = int(input())

nums = string.split(', ')
n = beggars
sum = 0
total = []

while n > 0:
    for i in range(beggars - n, len(nums), beggars):
        if i > len(nums) - 1:
            sum += 0
        else:
            sum += int(nums[i])
    total.append(sum)
    sum = 0
    n -= 1
print(total)
