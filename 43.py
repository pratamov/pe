from itertools import permutations

sums = 0
permutations = [''.join(p) for p in list(permutations('1234567890'))]
for p in permutations:
    if int(p[1:1+3]) % 2 == 0 and \
        int(p[2:2+3]) % 3 == 0 and \
        int(p[3:3+3]) % 5 == 0 and \
        int(p[4:4+3]) % 7 == 0 and \
        int(p[5:5+3]) % 11 == 0 and \
        int(p[6:6+3]) % 13 == 0 and \
        int(p[7:7+3]) % 17 == 0:
            print(p)
            sums += int(p)
print(sums)