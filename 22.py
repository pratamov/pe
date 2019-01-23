import urllib.request

with urllib.request.urlopen("https://projecteuler.net/project/resources/p022_names.txt") as url:
    lists = url.readlines()[0].decode("utf-8").split(',')
    lists.sort()
    lists = [s.replace('"', '') for s in lists]
    chars_value = {
        'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I': 9, 'J': 10,
        'K':11, 'L': 12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T': 20,
        'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26
    }
    total = 0
    for idx, s in enumerate(lists):
        total += sum([chars_value[c] for c in s]) * (idx + 1)
    print(total)
