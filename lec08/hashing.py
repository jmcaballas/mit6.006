from random import randint, randrange, getrandbits


class Hash:
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

    def _division_method(self, key):
        return key % self.size

    def _universal_hash(self, key):
        hash_value = hash(key)
        return ((self.a * hash_value + self.b) % self.p) % self.size

    def insert(self, key, value, hash_func="division"):
        if hash_func == "division":
            index = self._division_method(key)
        elif hash_func == "universal":
            index = self._universal_hash(key)
        else:
            raise ValueError("Invalid hash function.")

        self.hash_table[index].append((key, value))

    def delete(self, key, hash_func="division"):
        if hash_func == "division":
            index = self._division_method(key)
        elif hash_func == "universal":
            index = self._universal_hash(key)
        else:
            raise ValueError("Invalid hash function.")

        bucket = self.hash_table[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return

    def search(self, key, hash_func="division"):
        if hash_func == "division":
            index = self._division_method(key)
        elif hash_func == "universal":
            index = self._universal_hash(key)
        else:
            raise ValueError("Invalid hash function.")

        bucket = self.hash_table[index]

        return next((v for k, v in bucket if k == key), None)


hash_table = Hash(5)

hash_table.insert(78, "Value 78", hash_func="division")
hash_table.insert("abc", "Value abc", hash_func="universal")

print(hash_table.search(78, hash_func="division"))
print(hash_table.search("abc", hash_func="universal"))

hash_table.delete(78, hash_func="division")
hash_table.delete("abc", hash_func="universal")

print(hash_table.search(78, hash_func="division"))
print(hash_table.search("abc", hash_func="universal"))
