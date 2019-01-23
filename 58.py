def execute():
    bound = 100_000_000
    primes = [i for i in range(bound)]
    n = 2
    while n < bound/2:
        if primes[n] > 1:
            for i in range(n+n, bound, n):
                primes[i] = 0
        n += 1

    step = 2
    n = 1
    counter = 1
    prime_count = 0

    while True:
        for i in range(4):
            n += step
            counter += 1
            prime_count += 1 if primes[n] > 0 else 0
        step += 2
        if prime_count / counter < 0.1:break
        else:
            print(step/2, prime_count / counter)

    print(step - 1)
