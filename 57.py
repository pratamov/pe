from decimal import Decimal
from math import gcd

temporary = [None for i in range(1_002)]

def addition(tupple_a, tupple_b):
    lcm = tupple_a[1] * tupple_b[1] // gcd(tupple_a[1], tupple_b[1])
    return (
        int(tupple_a[0]*(lcm / tupple_a[1])) +
        int(tupple_b[0]*(lcm / tupple_b[1])),
        lcm
    )

def divide(tupple_a, tupple_b):
    result = (tupple_a[0]*tupple_b[1], tupple_a[1]*tupple_b[0])
    gcd_ = gcd(result[0], result[1])
    return (int(result[0]/gcd_), int(result[1]/gcd_))

def func(n):
    if n <= 1:
        return (3, 2)
    elif temporary[n] is not None:
        return temporary[n]
    else:
        fraction = addition((1, 1), divide((1, 1), addition((1, 1), func(n-1))))
        temporary[n] = fraction
        return fraction

count_more_numerator = 0
for i in range(1_001):
    fraction = func(i)
    if len(str(fraction[0])) > len(str(fraction[1])):
        print(fraction)
        count_more_numerator += 1

print(count_more_numerator)
