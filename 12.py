bound = 100_000_000
primes = [i for i in range(bound)]
n = 2
while n < bound/2:
    if primes[n] > 1:
        for i in range(n+n, bound, n):
            primes[i] = 0
    n += 1
primes = [p for p in primes if p > 1]

max_divisors = 0
x,y = 1,1
while True:
    x += 1
    y += x
    y_ = y
    pc = 0
    divisors = 1
    if y in primes:
        divisors = 2
    else:
        while primes[pc] <= y and pc < len(primes):
            v = 0
            while y_ % primes[pc] == 0 or y_ not in primes:
                y_ = int(y_ / primes[pc])
                v += 1
            if v>0:
                divisors *= (v+1)
            pc += 1
    if max_divisors < divisors:
        max_divisors = divisors
        print(x, y, divisors)
    if divisors > 500: break