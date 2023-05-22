from random import randrange, getrandbits

# https://medium.com/@ntnprdhmm/how-to-generate-big-prime-numbers-miller-rabin-49e6e6af32fb
def is_prime(n, k=128):
    if n in [2, 3]:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    s = 0
    r = n - 1
    while r & 1 == 0:
        s += 1
        r //= 2
    for _ in range(k):
        a = randrange(2, n - 1)
        x = pow(a, r, n)
        if x not in [1, n - 1]:
            j = 1
            while j < s and x != n - 1:
                x = pow(x, 2, n)
                if x == 1:
                    return False
                j += 1
            if x != n - 1:
                return False
    return True


def generate_prime_candidate(length):
    p = getrandbits(length)
    p |= (1 << length - 1) | 1
    return p


def generate_prime_number(length=1024):
    p = 4
    while not is_prime(p, 128):
        p = generate_prime_candidate(length)
    return p


def string_matching_simple(s, t):
    return any(s == t[i : i + len(s)] for i in range(len(t) - len(s)))


class RollingHash:
    def __init__(self, length, base=256):
        self.u = 0
        self.p = generate_prime_number()
        self.base = base
        self.exp = (self.base ** (length - 1)) % self.p

    def append(self, c):
        self.u = (self.u * self.base + ord(c)) % self.p

    def skip(self, c):
        self.u = (self.u - ord(c) * self.exp) % self.p


def string_matching_karp_rabin(s, t):
    rs = RollingHash(len(s))
    rt = RollingHash(len(s))

    for c in s:
        rs.append(c)
    for c in t[: len(s)]:
        rt.append(c)
    if rs.u == rt.u:
        return True
    for i in range(len(s), len(t)):
        rt.skip(t[i - len(s)])
        rt.append(t[i])
        if rs.u == rt.u:
            return True
    return False


print(string_matching_simple("fox", "The quick brown fox jumps over the lazy dog"))
print(string_matching_simple("cat", "The quick brown fox jumps over the lazy dog"))
print(string_matching_karp_rabin("fox", "The quick brown fox jumps over the lazy dog"))
print(string_matching_karp_rabin("cat", "The quick brown fox jumps over the lazy dog"))
