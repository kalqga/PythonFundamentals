cost = float(input())
num_of_months = int(input())

collected = 0.0


for i in range(1, num_of_months + 1):

    if i % 2 != 0:
        collected -= collected * 0.16
    elif i % 4 == 0:
        collected += collected * 0.25
    collected += cost * 0.25

if collected >= cost:
    print(f"Bravo! You can go to Disneyland and you will have {(collected - cost):.2f}lv. for souvenirs.")
else:
    print(f"Sorry. You need {(cost - collected):.2f}lv. more.")
