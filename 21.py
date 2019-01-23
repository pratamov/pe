lists = [sum([i for i in range(1, n) if n % i == 0]) for n in range(10_000)]
amicable = [n for index, n in enumerate(lists) if n < len(lists) and lists[n] == index and n != index]
print(sum(amicable))