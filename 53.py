from itertools import combinations

def combination_more_than(n, r, bound):
    num = [v for v in range((n-r)+1, n+1)]
    den = [v for v in range(1, r+1)]
    value = 1
    for v in num:
        value = value*v
    for v in den:
        value = int(value/v)
    return value > bound

value = [combination_more_than(n, r, 1_000_000)
         for n in range(101) for r in range(n)]
value = [v for v in value if v is True]
print(len(value))
