result = 1
power = 1
while True:
    base = 2
    while len(str(base**power)) <= power:
        if len(str(base**power)) == power:
            result += 1
        base += 1
    if power > 100:
        break
    power += 1
print(result)