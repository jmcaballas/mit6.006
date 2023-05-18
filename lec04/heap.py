def max_heapify(arr, i):
    current_max = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < len(arr) and arr[current_max] < arr[left]:
        current_max = left
    if right < len(arr) and arr[current_max] < arr[right]:
        current_max = right
    if current_max != i:
        temp = arr[i]
        arr[i] = arr[current_max]
        arr[current_max] = temp
        max_heapify(arr, current_max)


def build_max_heap(arr):
    for i in range(len(arr) // 2 - 1, -1, -1):
        max_heapify(arr, i)


arr = [7, 1, 4, 6, 3, 5, 2]
build_max_heap(arr)
print(arr)
