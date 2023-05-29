def text_justify(words, page_width):
    n = len(words)
    DP = {}
    DP[n] = 0
    parents = {}

    def badness(i, j):
        total_length = sum(len(words[k]) for k in range(i, j))
        if total_length > page_width:
            return float("inf")
        else:
            return (page_width - total_length) ** 3

    for i in range(n - 1, -1, -1):
        min_badness = float("inf")
        for j in range(i + 1, n + 1):
            current_badness = badness(i, j) + DP[j]
            if current_badness < min_badness:
                min_badness = current_badness
                parents[i] = j

        DP[i] = min_badness

    return DP[0], parents


words = [
    "Lorem",
    "ipsum",
    "dolor",
    "sit",
    "amet",
    "consectetur",
    "adipiscing",
    "elit",
    "Mauris",
    "id",
]
page_width = 15

result, parents = text_justify(words, page_width)
print(result)
print(parents)
