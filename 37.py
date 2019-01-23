bound = 1_000_000
primes = [i for i in range(bound)]
n = 2
while n < bound/2:
    if primes[n] > 1:
        for i in range(n+n, bound, n):
            primes[i] = 0
    n += 1
print(len(primes))
primes = [p for p in primes if str(p)[0] in ['2', '3', '5', '7'] and str(p)[-1:] in ['2', '3', '5', '7']]
print(len(primes))

for p in primes[0:20]:
    p_ = [c for c in list(str(p))]
    p__ = [''.join(p_[0:i]) for i in range(1, len(p_))]
    print(p__)