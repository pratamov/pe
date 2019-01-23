bound = 1_000_000
primes = [i for i in range(bound)]
n = 2
while n < bound/2:
    if primes[n] > 1:
        for i in range(n+n, bound, n):
            primes[i] = 0
    n += 1
primes = [p for p in primes if p > 1]
primes = [p for p in primes if all(c in ['1','3','7','9'] for c in str(p)) or p < 10]

circulars = 0
for i in primes:
    if i < 10:
        circulars += 1
    else:
        is_circular = True
        i_ = i
        while int(str(i_)[-1] + str(i_)[:-1]) != i and i_ > 10:
            if int(str(i_)[-1] + str(i_)[:-1]) not in primes:
                is_circular = False
                break
            i_ = int(str(i_)[-1] + str(i_)[:-1])
        if is_circular:
            print(i)
            circulars += 1

print(circulars)