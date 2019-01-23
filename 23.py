class BreakLoop(Exception):
    pass

divisor = [sum([n for n in range(1, i) if i % n == 0]) for i in range(28123)]
abundant = [idx for idx, val in enumerate(divisor) if val > idx]

result = 0
for i in range(28123):
    print('checking', i)
    is_sum_abundant_divisors = False
    for a in abundant:
        if a > i:
            break
        elif (i - a in abundant):
            is_sum_abundant_divisors = True
            break
    if is_sum_abundant_divisors is False:
        result += i

print(result)
