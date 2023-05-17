import random


def generate_random_array():
    # Generate a random length between 1 and 10
    n = random.randint(1, 10)
    # Generate a random array with values between 1 and 10
    return [random.randint(1, 10) for _ in range(n)]


def insertion_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[i]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
    return arr


def insertion_sort_key(arr):
    for i in range(len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


random_array = generate_random_array()
print(random_array)
print(insertion_sort(random_array))
print(insertion_sort_key(random_array))


def merge(left, right):
    arr = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr.append(left[i])
            i += 1
        else:
            arr.append(right[j])
            j += 1

    arr.extend(left[i:])
    arr.extend(right[j:])
    return arr


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # Recursive
    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


print(merge_sort(random_array))
