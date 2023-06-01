def difficulty_metric(f, p, q, g):
    if 1 < f < g and p > q:
        return 3
    if abs(p - q) > 12:
        return 3
    if f == g:
        return float("inf")
    if g in [4, 5]:
        return 2
    if f == 3 and g == 4:
        return 2
    return 2 if f == 4 and g == 3 else 1


def piano_fingering(notes, F=5):
    n = len(notes)
    DP = [[float("inf")] * (F + 1) for _ in range(n + 1)]

    for i in range(1, F + 1):
        DP[n - 1][i] = 0

    for i in range(n - 2, -1, -1):
        for f in range(1, F + 1):
            for g in range(1, F + 1):
                difficulty = difficulty_metric(notes[i], f, notes[i + 1], g)
                DP[i][f] = min(DP[i][f], DP[i + 1][g] + difficulty)

    return min(DP[0][1:])


notes = [1, 2, 3, 4, 5]
print(piano_fingering(notes))
