from math import sqrt

bound = 100_000
primes = [i for i in range(bound)]
n = 2
while n < bound/2:
    if primes[n] > 1:
        for i in range(n+n, bound, n):
            primes[i] = 0
    n += 1
primes = [p for p in primes if p > 1]

consecutive = 4
consecutive_temp = 0
consecutive_start = 0

for i in range(1, bound):
    if i not in primes:
        primes_ = []
        for p in primes:
            if p < i:
                primes_.append(p)
            else:
                break
        factors = sum([1 for p in primes_ if i % p == 0])
        if factors == consecutive:
            consecutive_temp += 1
            if consecutive_temp == 1: consecutive_start = i
        else:
            consecutive_temp = 0
            consecutive_start = 0
    else:
        consecutive_temp = 0
        consecutive_start = 0

    if consecutive_temp == consecutive:
        print(i)
        break
