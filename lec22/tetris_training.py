def tetris_training(pieces, w, h):
    n = len(pieces)
    DP = [[0] * (h + 1) for _ in range(n + 1)]
    parent = [[None] * (h + 1) for _ in range(n + 1)]

    for i in range(n - 1, -1, -1):
        for height in range(h + 1):
            for move in range(w):
                current_height = height + pieces[i][move]
                if current_height <= h:
                    score = DP[i + 1][current_height]
                else:
                    score = float("inf")

                if score >= DP[i][height]:
                    DP[i][height] = score
                    parent[i][height] = move

    moves = []
    height = 0
    for i in range(n):
        move = parent[i][height]
        moves.append(move)
        height += pieces[i][move]

    return moves


pieces = [
    [0, 0, 0, 1],
    [0, 0, 1, 1],
    [0, 1, 1, 1],
    [1, 1, 1, 1],
]
w = 4
h = 10

print(tetris_training(pieces, w, h))
