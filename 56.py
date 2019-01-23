max_digital_sum = 0
for a in range(100):
    for b in range(100):
        max_digital_sum = max(max_digital_sum, sum(
            [int(c) for c in str(a**b)]))
print(max_digital_sum)