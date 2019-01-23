pentagons = [n * (3*n-1) / 2 for n in range(10_000)]

print('calculating')
min_d = 99999999999
for idx1, p1 in enumerate(pentagons):
    for p2 in pentagons[idx1+1:]:
        if (p1 + p2) in pentagons and (p2 - p1) in pentagons:
            if min_d < p2-p1:
                print(p2-p1)
            min_d = min(min_d, p2-p1, p1)
print(min_d)
