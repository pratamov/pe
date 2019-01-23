from itertools import permutations

numbers = [''.join([str(i) for i in range(1,j)]) for j in range(11)]
permutations = [[''.join(p) for p in list(permutations(n)) if p != ''] for n in numbers]
permutations = [int(p) for row in permutations for p in row if p.strip() != '']
permutations.sort(reverse=True)

idx = 0
while idx < len(permutations):
    is_prime = True
    for i in range(2, int(permutations[idx]/2)):
        if permutations[idx] % i == 0:
            is_prime = False
            break
    if is_prime:
        print(permutations[idx], 'is prime')
        break
    else:
        print(permutations[idx])
    idx += 1