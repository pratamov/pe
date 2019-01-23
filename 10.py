numbers = [i for i in range(2_000_000)]
for n in range(2_000_000):
    if n > 1:
        m = n + n
        while(m < 2_000_000):
            numbers[m] = 0
            m += n
print(sum([n for n in numbers if n > 1]))