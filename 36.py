result = 0
for i in range(1_000_000):
    if str(i) == str(i)[::-1] and bin(i)[2:] == bin(i)[2:][::-1]:
        result += i
print(result)