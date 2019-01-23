from math import factorial
factorials = [factorial(i) for i in range(10)]

result = 0
n = 10
while n < sum(factorials):
    fac = [idx for idx, f in enumerate(factorials) if f < n]
    digits = [int(d) for d in str(n)]
    contains = sum([1 for i in digits if i not in fac])
    if contains == 0:
        if sum([factorials[int(i)] for i in str(n)]) == n:
            result += n
    n+=1
print(result)