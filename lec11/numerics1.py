def catalan_number(n):
    if n <= 1:
        return 1

    return sum(catalan_number(i) * catalan_number(n - 1 - i) for i in range(n))


print(catalan_number(3))
print(catalan_number(5))


def newton_method(f, f_prime, n, initial, delta=1e-6):
    x = initial

    while abs(f(x, n)) > delta:
        x = x - f(x, n) / f_prime(x)

    return x


def f(x, n):
    return x**2 - n


def f_prime(x):
    return 2 * x


print(f"Square Root of 2: {newton_method(f, f_prime, n=2, initial=1)}")
print(f"Square Root of 4: {newton_method(f, f_prime, n=4, initial=2, delta=1e-12)}")


def karatsuba(x, y, r=10):
    if x < r or y < r:
        return x * y

    n = max(len(str(x)), len(str(y)))
    n2 = n // 2

    x0 = x % r**n2
    x1 = x // r**n2
    y0 = y % r**n2
    y1 = y // r**n2

    z0 = karatsuba(x0, y0, r)
    z2 = karatsuba(x1, y1, r)
    z1 = karatsuba((x0 + x1), (y0 + y1), r) - z0 - z2

    return (z2 * (r ** (2 * n2))) + (z1 * (r**n2)) + z0


print(karatsuba(123456789, 987654321))
