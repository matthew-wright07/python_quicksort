import random

random_array = []

for i in range(1000):
    random_array.append(random.randint(0,1000))

left = []
right = []

for i in range(len(random_array)):
    if random_array[i] < len(random_array)/2:
        left.append(random_array[i])
    else:
        right.append(random_array[i])

for _ in range(len(left)-1):
    for i in range(len(left)-1):
        if left[i] > left[i+1]:
            inbetween = left[i]
            left[i] = left[i+1]
            left[i+1] = inbetween

for _ in range(len(right)-1):
    for i in range(len(right)-1):
        if right[i] > right[i+1]:
            inbetween = right[i]
            right[i] = right[i+1]
            right[i+1] = inbetween

final = left + right

print(final)