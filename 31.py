import itertools
from fractions import gcd

list(itertools.permutations([1, 2, 3]))

def coins(a, b, c, d, e, f, g, h):
    return a + 2*b + 5*c + 10*d + 20*e + 50*f + 100*g + 200*h

combinations = [(p1, p2, p5, p10, p20, p50, p100, p200) 
                for p1 in range(int(200/1) + 1)
                for p2 in range(int(200/2) + 1)
                for p5 in range(int(200/5) + 1)
                for p10 in range(int(200/10) + 1)
                for p20 in range(int(200/20) + 1)
                for p50 in range(int(200/50) + 1)
                for p100 in range(int(200/100) + 1)
                for p200 in range(int(200/200) + 1)
                if coins(p1, p2, p5, p10, p20, p50, p100, p200) == 0]

print(len(combinations))