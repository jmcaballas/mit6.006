def multiplication_cost(matrix1, matrix2):
    return len(matrix1) * len(matrix2[0]) * len(matrix1[0])


def parenthesization(matrix):
    n = len(matrix)
    DP = [[float("inf")] * (n + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        DP[i][i] = 0

    for length in range(2, n + 1):
        for i in range(1, n - length + 2):
            j = i + length - 1
            for k in range(i, j):
                cost = (
                    DP[i][k]
                    + DP[k + 1][j]
                    + multiplication_cost(matrix[i - 1 : k], matrix[k:j])
                )
                DP[i][j] = min(DP[i][j], cost)

    return DP[1][n]


matrix = [[0, 0], [1, 1], [2, 2]]
print(parenthesization(matrix))
