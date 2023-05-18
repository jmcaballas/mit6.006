import random


def generate_random_array():
    # Generate a random length between 1 and 10
    n = random.randint(1, 10)
    # Generate a random array with values between 1 and 10
    return [random.randint(1, 10) for _ in range(n)]


def max_heapify(arr, i, n):
    current_max = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[current_max] < arr[left]:
        current_max = left
    if right < n and arr[current_max] < arr[right]:
        current_max = right
    if current_max != i:
        temp = arr[i]
        arr[i] = arr[current_max]
        arr[current_max] = temp
        max_heapify(arr, current_max, n)


def build_max_heap(arr):
    for i in range(len(arr) // 2 - 1, -1, -1):
        max_heapify(arr, i, len(arr))


def heap_sort(arr):
    build_max_heap(arr)
    for i in range(len(arr) - 1, 0, -1):
        temp = arr[i]
        arr[i] = arr[0]
        arr[0] = temp
        max_heapify(arr, 0, i)


random_array = generate_random_array()
print(random_array)
heap_sort(random_array)
print(random_array)
