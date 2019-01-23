bound = 1_000_000
primes = [i for i in range(bound)]
n = 2
while n < bound/2:
    if primes[n] > 1:
        for i in range(n+n, bound, n):
            primes[i] = 0
    n += 1
primes = [p for p in primes if p > 1]

max_sum_length, max_sum_value = 1, 2
for p in primes:
    chances = [c for c in primes if c < p]
    sum_length = 0
    for start in range(len(chances)):
        n = start+1
        while True:
            if n > len(chances):
                break
            sums = sum([v for v in chances[start:n]])
            if sums > p:
                break
            elif sums == p:
                sum_length = max(sum_length, n - start)
                break
            n += 1
    if max_sum_length < sum_length:
        max_sum_length = sum_length
        max_sum_value = p
        print(max_sum_value, max_sum_length)

print(max_sum_value, max_sum_length)