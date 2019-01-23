bounds = 1_000_000

lengths = [0 for i in range(bounds*99)]
max_length, max_value = 1, 1
for i in range(1, bounds):
    number = i
    length = 1
    while number > 1:
        if number < bounds*99 and lengths[number] > 0:
            length += lengths[number]
            number = 1
        else:
            number = int(
                number / 2) if number % 2 == 0 else int(number * 3 + 1)
            length += 1
    lengths[number] = length
    if max_length < length:
        print(length, i)
        max_length, max_value = length, i

print(max_value)