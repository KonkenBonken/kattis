from math import log2, ceil

src = tuple(c.upper() for c in input() if c.isalpha())
chars = sorted(set(src), key=src.count, reverse=True)

if len(src) == 1:
    print(1)
    exit()

codes = []

for l in range(1, ceil(log2(len(chars))) + 3):
    for b in range(2**l):
        m = format(b, 'b').rjust(l, '0')
        char = m.count('0') + m.count('1')*3 + l-1 + 3
        codes.append(char)

codes.sort(reverse=True)

res = -3

for char in chars:
    res += codes.pop()*src.count(char)

print(res)
