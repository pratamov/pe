from math import log
upper_bound = 10_001 * int(log(10_001) + log(log(10_001)))
numbers = [i for i in range(upper_bound)]
for n in range(upper_bound):
    if n>1:
        c = n + n
        while(c < upper_bound):
            numbers[c] = 0
            c += n
primes = [n for n in numbers if n > 1]
print(primes[10_001 - 1])