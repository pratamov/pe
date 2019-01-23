n1, n2, idx = 1, 1, 2

while len(str(n2)) < 1000:
    n3 = n1+n2
    n1 = n2
    n2 = n3
    idx += 1

print(n1, n2, idx)