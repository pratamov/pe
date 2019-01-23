from itertools import permutations

bound = 9999
primes = [i for i in range(bound)]
n = 2
while n < bound/2:
    if primes[n] > 1:
        for i in range(n+n, bound, n):
            primes[i] = 0
    n += 1
primes = [p for p in primes if p < 10_000 and p > 999]

numbers = []
for p in primes:
    p_str = str(p)
    perm = [int(''.join(c)) for c in list(permutations(p_str))]
    perm = [v for v in perm if v < 10_000 and v > 999 and v > p and v in primes]
    for n in perm:
        if n + (n - p) in primes and n + (n - p) in perm:
            numbers.append(str(p) + str(n) + str(n + (n - p)))

print(numbers)