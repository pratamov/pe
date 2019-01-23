import urllib.request

with urllib.request.urlopen("https://projecteuler.net/project/resources/p042_words.txt") as url:
    lists = url.readlines()[0].decode("utf-8").split(',')
    lists = [s.replace('"', '') for s in lists]
    max_len = max([len(l) for l in lists])
    triangles = [int(n*(n+1) / 2) for n in range(max_len * 26)]

    chars_value = {
        'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10,
        'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20,
        'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26
    }
    '''
    for val, char in enumerate(chars_value):
        if val not in triangles:
            chars_value[char] = -999999
    '''

    values = [sum([chars_value[c] for c in name]) for name in lists]
    result = sum([1 for v in values if v in triangles])
    print(result)