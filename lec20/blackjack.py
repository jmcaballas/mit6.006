def blackjack(deck):
    n = len(deck)
    memo = [0] * (n + 1)

    def BJ(i):
        if n - i < 4:
            return 0
        if memo[i] != 0:
            return memo[i]

        outcomes = []
        for p in range(2, n - i - 2):
            player = sum(deck[i : i + p + 2 : 2])
            if player > 21:
                outcomes.append(-1 + BJ(i + p + 2))
                break
            for d in range(2, n - i - p):
                dealer = sum(deck[i + 1 : i + p + d + 2 : 2])
                if dealer >= 17:
                    break
                if dealer > 21:
                    dealer = 0
                outcome = 1 if player > dealer else (-1 if player < dealer else 0)
                outcomes.append(outcome + BJ(i + p + d))

        memo[i] = max(outcomes)
        return memo[i]

    return BJ(0)


deck = [10, 5, 8, 6, 7, 3, 2, 9, 4, 1]
print(blackjack(deck))
