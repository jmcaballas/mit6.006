import random


def generate_random_1D_array():
    # Generate a random length between 1 and 10
    n = random.randint(1, 10)
    # Generate a random array with values between 1 and 10
    return [random.randint(1, 10) for _ in range(n)]


random_array = generate_random_1D_array()
print(random_array)


def peak_finder_1D(arr):
    n = len(arr)
    mid = n // 2

    if n == 1:
        return arr[0]
    if n == 2:
        return max(arr[0], arr[1])
    if arr[mid] < arr[mid - 1]:
        return peak_finder_1D(arr[:mid])
    return peak_finder_1D(arr[mid:]) if arr[mid] < arr[mid + 1] else arr[mid]


print(peak_finder_1D(random_array))


def generate_random_2D_matrix():
    # Generate a random number of rows between 1 and 5
    rows = random.randint(1, 5)
    # Generate a random number of columns between 1 and 5
    cols = random.randint(1, 5)
    # Generate a random 2D matrix with values between 1 and 100
    return [[random.randint(1, 100) for _ in range(cols)] for _ in range(rows)]


random_2D_matrix = generate_random_2D_matrix()
for row in random_2D_matrix:
    print(row)


def peak_finder_2D(matrix):
    n = len(matrix)
    mid_row = matrix[n // 2]
    mid_row_max = max(mid_row)
    i = mid_row.index(mid_row_max)

    if n == 1:
        return mid_row_max
    if n == 2:
        return max(mid_row_max, matrix[0][i])
    if mid_row_max < matrix[n // 2 - 1][i]:
        return peak_finder_2D(matrix[: n // 2])
    if mid_row_max < matrix[n // 2 + 1][i]:
        return peak_finder_2D(matrix[n // 2 :])
    return mid_row_max


print(peak_finder_2D(random_2D_matrix))
