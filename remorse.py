src = tuple(c.upper() for c in input() if c.isalnum())
chars = reversed(sorted(set(src), key=src.count))

b, res = 0, -3
for c in chars:
    m = format(b, 'b')
    res += 3 + m.count('0') + m.count('1')*3 + len(m)-1
    b += 1

print(res)
