stop = 9
while sum([int(n)**5 for n in str(stop)]) > stop:
    stop = stop * 10 + 9
result = 0
for i in range(2, stop):
    if sum([int(n)**5 for n in str(i)]) == i:
        result += i
print(result)