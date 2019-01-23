from itertools import permutations

class BreakLoop(Exception): pass

perm = [int(''.join(l)) for l in list(permutations('123456789'))]
perm.sort(reverse=True)

try:
    for item in perm:
        item_ = str(item)
        possibles = [[str(n) for n in [m*first for m in range(1, 10)]] for first in [int(item_[0:i]) for i in range(1, 9)]]
        for p in possibles:
            for i in range(1, len(possibles)):
                if len(''.join(p[0:i])) == 9:
                    if item == int(''.join(p[0:i])):
                        print(item)
                        raise BreakLoop
except BreakLoop:
    pass