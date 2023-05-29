def fibonacci_naive(n):
    return 1 if n <= 2 else fibonacci_naive(n - 1) + fibonacci_naive(n - 2)


def fibonacci_memoized(n):
    memo = {}
    if n in memo:
        return n
    if n <= 2:
        return 1
    f = fibonacci_memoized(n - 1) + fibonacci_memoized(n - 2)
    memo[n] = f
    return f


def fibonacci_bottom_up(n):
    fib = {}
    for k in range(1, n + 1):
        f = 1 if k <= 2 else fib[k - 1] + fib[k - 2]
        fib[k] = f
    return fib[n]


print(
    fibonacci_naive(1),
    fibonacci_naive(2),
    fibonacci_naive(3),
    fibonacci_naive(4),
    fibonacci_naive(5),
)
print(
    fibonacci_memoized(1),
    fibonacci_memoized(2),
    fibonacci_memoized(3),
    fibonacci_memoized(4),
    fibonacci_memoized(5),
)
print(
    fibonacci_bottom_up(1),
    fibonacci_bottom_up(2),
    fibonacci_bottom_up(3),
    fibonacci_bottom_up(4),
    fibonacci_bottom_up(5),
)
