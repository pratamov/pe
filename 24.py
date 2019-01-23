from itertools import permutations

perms = [int(''.join(i)) for i in list(permutations('0123456789'))]
perms.sort()
print(perms[1_000_000 - 1])