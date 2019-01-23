from math import sqrt
from decimal import Decimal

def derivation(a, b, c):
    a = Decimal(a)
    b = Decimal(b)
    c = Decimal(c)

    d1 = (-b + Decimal(sqrt(b**2 - 4*a*c))) / 2*a
    d2 = (-b - Decimal(sqrt(b**2 - 4*a*c))) / 2*a
    return [n for n in [d1, d2] if n > 0 and n%1 == 0]

n = 1

while True:
    # T = n * (n+1) / 2 = (n^2) + n - 2*m
    # P = n * (3*n - 1) / 2 = (3*n^2) - n - 2*m

    h = n * (2*n-1)

    dt = derivation(1, 1, -2*h)
    dp = derivation(3, -1, -2*h)

    if len(dt) > 0 and len(dp) > 0:
        print(h, int(dt[0]), dt, dp)

    if n > 146000:
        break
    n += 1
