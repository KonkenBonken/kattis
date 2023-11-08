src = tuple(c.upper() for c in input() if c.isalnum())
chars = tuple(reversed(sorted(set(src), key=src.count)))

b, i, res = 0, 0, -3

while i < len(chars):
    m = format(b, 'b')
    res += (3 + m.count('0') + m.count('1')*3 + len(m)-1) * src.count(chars[i])
    if m.count('0') == 0:
        i += 1
        res += (3 + len(m)+1 + len(m)) * src.count(chars[i])
    b += 1
    i += 1

print(res)
