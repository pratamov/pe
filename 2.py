fibo = [1, 1]
while fibo[-1] < 4_000_000: fibo.append(sum(fibo[-2:]))
print(sum([f for f in fibo[:-1][1:] if f%2 == 0]))