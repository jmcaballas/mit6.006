def edit_distance(x, y):
    DP = [[0] * (len(y) + 1) for _ in range(len(x) + 1)]

    for i in range(len(x) + 1):
        DP[i][len(y)] = len(x) - i
    for j in range(len(y) + 1):
        DP[len(x)][j] = len(y) - j

    for i in range(len(x) - 1, -1, -1):
        for j in range(len(y) - 1, -1, -1):
            if x[i] == y[j]:
                DP[i][j] = DP[i + 1][j + 1]
            else:
                DP[i][j] = min(DP[i + 1][j], DP[i][j + 1], DP[i + 1][j + 1]) + 1

    return DP[0][0]


print(edit_distance("horse", "ros"))
print(edit_distance("intention", "execution"))
