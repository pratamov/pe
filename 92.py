def next_chain(number):
    return sum([int(i)*int(i) for i in str(number)])

def find_last_chain(number):
    if number == 1 or number == 89: return number, []
    numbers = [number]
    while True:
        if next_chain(number) == 1:
            return 1, numbers
        elif next_chain(number) == 89:
            return 89, numbers
        else:
            number = next_chain(number)
            numbers.append(number)

def find_starting_number_endup_to_89_below(n):
    temp = [0 for i in range(n)]

    for i in range(n-1, 0, -1):
        if temp[i] == 0:
            if i % 100_000 == 0:
                print(i, sum([1 for t in temp if t == 89]))
            last, numbers = find_last_chain(i)
            for n in numbers:
                if n < len(temp):
                    temp[n] = last
    return sum([1 for t in temp if t == 89])

print(find_starting_number_endup_to_89_below(10_000_001))