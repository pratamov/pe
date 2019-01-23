from math import gcd
product_numerator = 1
product_denominator = 1

for n1 in range(1, 10):
    for n2 in range(1, 10):
        for d2 in [x for x in [1,2,3,4,5,6,7,8,9] if x not in [n1, n2]]:
            if (n1*10 + n2) / (n1*10 + d2) == n2 / d2 and n2 / d2 < 1:
                product_numerator *= n2
                product_denominator *= d2
            if (n2*10 + n1) / (n1*10 + d2) == n2 / d2 and n2 / d2 < 1:
                product_numerator *= n2
                product_denominator *= d2
            if (n1*10 + n2) / (d2*10 + n1) == n2 / d2 and n2 / d2 < 1:
                product_numerator *= n2
                product_denominator *= d2
            if (n2*10 + n1) / (d2*10 + n1) == n2 / d2 and n2 / d2 < 1:
                product_numerator *= n2
                product_denominator *= d2

print(int(product_denominator / gcd(product_denominator, product_numerator)))