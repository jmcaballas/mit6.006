import random


def generate_random_array():
    # Generate a random array with 8 values between 1 and 10
    return [random.randint(1, 1000) for _ in range(8)]


def counting_sort(arr):
    max_value = max(arr)
    L = [0] * (max_value + 1)
    output = []

    for i in arr:
        L[i] += 1
    for j in range(len(L)):
        output.extend([j] * L[j])

    return output


def radix_sort(arr):
    max_value = max(arr)
    base = 1
    while max_value // base > 0:
        arr = counting_sort(arr)
        base *= 10
    return arr


random_array = generate_random_array()
print(random_array)
print(counting_sort(random_array))
print(radix_sort(random_array))
