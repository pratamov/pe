bound = 50_000
primes = [i for i in range(bound)]
n = 2
while n < bound/2:
    if primes[n] > 1:
        for i in range(n+n, bound, n):
            primes[i] = 0
    n += 1
primes = [p for p in primes if p > 1]

def polynom(a, b, n):
    return n*n + a*n + b

print("calculating")
bound = 1_000
a_b = [(a, b) for a in range(-bound+1, bound) for b in range(-a, bound+1)
       if polynom(a, b, 0) in primes and
       polynom(a, b, 1) in primes and
       polynom(a, b, 2) in primes and
       polynom(a, b, 3) in primes and
       polynom(a, b, 4) in primes]

max_len, max_val = 0, 0
for a, b in a_b:
    n = 5
    while polynom(a, b, n) in primes:
        n += 1
    if max_len < n:
        max_len = n
        max_val = abs(a*b)
        print(a, b, n, max_val)
