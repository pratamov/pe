number = 1
for i in range(1000):
    number *= 2
print(sum([int(i) for i in str(number)]))