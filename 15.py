def count(x = 2, y = 2):
    if x < 1 and y < 1:
        return 1
    elif x > 0 and y == 0:
        return count(x-1, y)
    elif x == 0 and y > 0:
        return count(x, y-1)
    else:
        return count(x-1, y) + count(x, y-1)

print(count(20, 20))