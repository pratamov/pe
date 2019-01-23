from itertools import permutations, combinations

lists = []
for i in range(1, 10):
    for len_ in range(1, i+1):
        list_ = list(combinations([str(v) for v in range(1, i+1)], len_))
        #list_ = [int(''.join(l)) for l in list_]
        lists.append(list_)

print(len(lists))
'''
lists = [l for l in lists if len(l) > 5]

valids = []
for row in lists:
    for item in row:
        if set([item*2, item*3]).issubset(set(row)):
            print(item)
            print(row)
            valids.append([item, item*2, item*3, item*4, item*5, item*6])

print(valids)
'''