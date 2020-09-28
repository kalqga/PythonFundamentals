n = int(input())
capacity = 255
total_liters = 0

for i in range(0, n):
    liters = int(input())
    total_liters += liters
    if total_liters > capacity:
        print("Insufficient capacity!")
        total_liters -= liters
        liters = int(input())
        total_liters += liters
        print(total_liters)
        break
#########################################################################################