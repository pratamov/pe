value_solution, max_solutions = 0, 0
for p in range(1, 1_001):
    solutions = []
    for a in range(1, int(p/2)):
        for b in range(1, p - a):
            c = p - a - b
            abc = [a, b, c]
            abc.sort()
            if abc[2]**2 == (abc[1]**2 + abc[0]**2):
                if a*b*c not in solutions:
                    solutions.append(a*b*c)
    if max_solutions < len(solutions):
        max_solutions = len(solutions)
        value_solution = p
        print(p)
print(value_solution)