n = int(input())
positives = []
negatives = []
positive_count = 0
negative_count = 0

for i in range(n):
    current_number = int(input())

    if current_number >= 0:
        positives.append(current_number)
        positive_count += 1
    else:
        negatives.append(current_number)
        negative_count += current_number

print(positives)
print(negatives)
print(f'Count of positives: {positive_count}. Sum of negatives: {negative_count}')
