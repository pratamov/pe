from math import gcd
result = 1
for n in range(2, 20+1): result = int(result*n / gcd(result, n))
print(result)