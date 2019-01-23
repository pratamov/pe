from itertools import permutations, combinations
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]

products = []
a = [l for n in range(1, 9) for l in list(combinations(digits, n))]
a = [list(l) for l in a]
for a_val in a:
    digits_ = [d for d in digits if d not in a_val]
    b = [l for n in range(1, 9) for l in list(combinations(digits_, n))]
    b = [list(l) for l in b]
    for b_val in b:
        digits__ = [d for d in digits_ if d not in b_val]
        remain_len = 9 - len(a_val) - len(b_val)
        c = [l for l in list(combinations(digits__, remain_len))]
        c = [list(l) for l in c]
        for c_val in c:
            if len(c_val):
                values = [int(''.join([str(i) for i in a_val])),
                          int(''.join([str(i) for i in b_val])),
                          int(''.join([str(i) for i in c_val]))]
                values.sort()
                if values[2] not in products:
                    products.append(values)
                if 7254 in values and 39 in values and 186 in values:
                    print(values)
#print((products))
