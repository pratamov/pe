layers = int((1001-1)/2)
n = 1
result = 1
for i in range(1, layers + 1):
    diff = 2*i
    for j in range(4):
        n += diff
        result += n
print(result)