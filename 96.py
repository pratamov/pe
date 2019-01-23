from json import dumps
from copy import deepcopy
import urllib.request

horizontals = [[i for i in range(c, c+9)] for c in range(1, 81, 9)]
verticals = [[horizontals[i][row] for i in range(9)] for row in range(9)]
clusters = [
    [i for i in range(1, 28) if (i+9) % 9 == 1 or (i+9) %
     9 == 2 or (i+9) % 9 == 3],
    [i for i in range(1, 28) if (i+9) %
     9 == 4 or (i+9) % 9 == 5 or (i+9) % 9 == 6],
    [i for i in range(1, 28) if (i+9) %
     9 == 7 or (i+9) % 9 == 8 or (i+9) % 9 == 0],
    [i for i in range(28, 55) if (i+9) % 9 == 1 or (i+9) %
     9 == 2 or (i+9) % 9 == 3],
    [i for i in range(28, 55) if (i+9) %
     9 == 4 or (i+9) % 9 == 5 or (i+9) % 9 == 6],
    [i for i in range(28, 55) if (i+9) %
     9 == 7 or (i+9) % 9 == 8 or (i+9) % 9 == 0],
    [i for i in range(55, 82) if (i+9) % 9 == 1 or (i+9) %
     9 == 2 or (i+9) % 9 == 3],
    [i for i in range(55, 82) if (i+9) %
     9 == 4 or (i+9) % 9 == 5 or (i+9) % 9 == 6],
    [i for i in range(55, 82) if (i+9) %
     9 == 7 or (i+9) % 9 == 8 or (i+9) % 9 == 0]
]

def solve(inputs_, index=0):
    if index > 80:
        return inputs_
    elif inputs_[index] == 0:
        taken = [inputs_[i-1] for i in [val for val in horizontals if index+1 in val][0]] + \
                [inputs_[i-1] for i in [val for val in verticals if index+1 in val][0]] + \
                [inputs_[i-1] for i in [val for val in clusters if index+1 in val][0]]
        avail = [val for val in range(1,10) if val not in taken]
        for guess in avail:
            inputs_copy = deepcopy(inputs_)
            inputs_copy[index] = guess
            outputs = solve(inputs_copy, index+1)
            if outputs is not None:
                return outputs
    else:
        inputs_copy = deepcopy(inputs_)
        return solve(inputs_copy, index+1)


with urllib.request.urlopen("https://projecteuler.net/project/resources/p096_sudoku.txt") as url:
    lines = [l.decode("utf-8").rstrip('\n') for l in url.readlines() if l is not '']
    inputs = [lines[i:i+9] for i in range(1, len(lines), 10)]
    sums = 0
    for record in inputs:
        solution = solve([int(i) for i in ''.join([d for d in record])])[0:3]
        sums += int(''.join([str(i) for i in solution]))
    print(sums)
