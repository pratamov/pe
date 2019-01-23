def spell(number):
    ones = ["", "one", "two", "three", "four", "five",
               "six", "seven", "eight", "nine", "ten", "eleven",
               "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
               "seventeen", "eighteen", "nineteen"]
    tens = ["", "ten", "twenty", "thirty", "forty",
            "fifty", "sixty", "seventy", "eighty", "ninety"]
    if number in range(0, 20):
        return ones[number]
    elif number < 100:
        return tens[int(number/10)] + spell(number % 10)
    elif number < 1000:
        remainder = "and" + spell(number % 100) if number % 100 > 0 else ""
        return ones[int(number/100)] + "hundred" + remainder
    elif number == 1000:
        return "onethousand"

print(sum([len(s) for i in range(1,1001) for s in spell(i)]))