from math import sqrt

bound = 10_000
primes = [i for i in range(bound)]
n = 2
while n < bound/2:
    if primes[n] > 1:
        for i in range(n+n, bound, n):
            primes[i] = 0
    n += 1
primes = [p for p in primes if p > 1]

for i in range(3, bound, 2):
    valid = False
    if i in primes:
        valid = True
    else:
        for p_ in [p for p in primes if p < i]:
            if sqrt((i - p_)/2) == int(sqrt((i - p_)/2)):
                valid = True
    if valid is False:
        print(i, 'invalid goldbach')
        break