import math

inputs = 600851475143
numbers = [n for n in range(math.ceil(math.sqrt(inputs)))]
for n in range(2, len(numbers)):
    if numbers[n] > 1:
        m = n + n
        while m < numbers[-1]:
            numbers[m] = 0
            m = m + n
for p in reversed([n for n in numbers if n > 0]):
    if inputs % p == 0:
        print(p)
        break
