sums = 0
for i in range(1, 1000):
    powers = 1
    for j in range(i):
        powers = (powers * i) % 10_000_000_000
    sums += powers
print(sums % 10_000_000_000)