from random import randint, randrange, getrandbits


class Probing:
    def __init__(self, size):
        self.size = size
        self.hash_table = [[] for _ in range(size)]
        self.a = randint(0, size - 1)
        self.b = randint(0, size - 1)
        self.p = self.generate_prime_number(length=256)

    # https://medium.com/@ntnprdhmm/how-to-generate-big-prime-numbers-miller-rabin-49e6e6af32fb
    def is_prime(self, n, k=128):
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

    def generate_prime_candidate(self, length):
        p = getrandbits(length)
        p |= (1 << length - 1) | 1
        return p

    def generate_prime_number(self, length=1024):
        p = 4
        while not self.is_prime(p, 128):
            p = self.generate_prime_candidate(length)
        return p

    def _universal_hash(self, key):
        hash_value = hash(key)
        return ((self.a * hash_value + self.b) % self.p) % self.size

    def _linear_probe(self, attempt, value):
        return (self._universal_hash(value) + attempt) % self.size

    def _double_hash(self, attempt, value):
        return (
            self._universal_hash(value) + self._universal_hash(value) + 1 * attempt
        ) % self.size

    def insert(self, value):
        index = self._double_hash(0, value)
        attempt = 0
        while self.hash_table[index]:
            attempt += 1
            index = self._double_hash(attempt, value)
        self.hash_table[index] = value

    def delete(self, value):
        index = self._double_hash(0, value)
        attempt = 0
        while attempt < self.size:
            if self.hash_table[index] == value:
                self.hash_table[index] = "DeleteMe"
                return
            attempt += 1
            index = self._double_hash(attempt, value)
        return

    def search(self, value):
        index = self._double_hash(0, value)
        attempt = 0
        while attempt < self.size:
            if self.hash_table[index] == value:
                return self.hash_table[index]
            attempt += 1
            index = self._double_hash(attempt, value)
        return


hash_table = Probing(10)
hash_table.insert(42)
hash_table.insert(7)
hash_table.insert(15)
print(hash_table.search(7))
hash_table.delete(7)
print(hash_table.search(7))
