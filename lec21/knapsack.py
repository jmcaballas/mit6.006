def knapsack(S, n, sizes, values, DP):
    if (n, S) in DP:
        return DP[n, S]
    if n == 0 or S == 0:
        result = (0, [])
    elif sizes[n - 1] > S:
        result = knapsack(S, n - 1, sizes, values, DP)
    else:
        without_current = knapsack(S, n - 1, sizes, values, DP)
        with_current = knapsack(S - sizes[n - 1], n - 1, sizes, values, DP)

        if values[n - 1] + with_current[0] > without_current[0]:
            result = (values[n - 1] + with_current[0], with_current[1] + [n - 1])
        else:
            result = without_current

    DP[n, S] = result
    return result


S = 10
sizes = [2, 3, 4, 5]
values = [3, 4, 5, 6]
n = len(sizes)
DP = {}

max_value, subset = knapsack(S, n, sizes, values, DP)
print(max_value)
print(subset)
