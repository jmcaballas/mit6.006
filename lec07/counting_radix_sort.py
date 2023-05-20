import random


def generate_random_array():
    # Generate a random length between 1 and 10
    n = random.randint(1, 10)
    # Generate a random array with values between 1 and 10
    return [random.randint(1, 10) for _ in range(n)]


def counting_sort(arr):
    max_value = max(arr)
    L = [[] for _ in range(max_value + 1)]
    for i in arr:
        L[i].append(i)

    output = []
    for item in L:
        output.extend(item)
    return output


random_array = generate_random_array()
print(random_array)
print(counting_sort(random_array))
