numbers = ""
for i in range(1_000_000):
    numbers += str(i)
print(int(numbers[1])*int(numbers[10])*int(numbers[100])
      * int(numbers[1_000])*int(numbers[10_000])*int(numbers[100_000])
      * int(numbers[1_000_000]))