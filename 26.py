from decimal import Decimal, getcontext

getcontext().prec = 100

def get_recurring_cycle(d, n=1):
    while n < d:
        n *= 10

    d_list = []
    while n not in d_list:
        d_list.append(n)
        n = (n - (d*int(n/d))) * 10
    result = 0 if 0 in d_list else len(d_list) - d_list.index(n)
    return result

max_recurring, val_recurring = 0, 0
for i in range(1, 1000):
    recurring = get_recurring_cycle(i)
    if max_recurring < recurring:
        max_recurring = recurring
        val_recurring = i

print(val_recurring)