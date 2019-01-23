power_2 = 1
for i in range(7830457):
    power_2 = (power_2*2) % 10000000000

print((28433 * power_2 + 1) % 10000000000)
