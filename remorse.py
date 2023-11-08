src = tuple(c.upper() for c in input() if c.isalpha())
chars = sorted(set(src), key=src.count)

if len(src) == 1:
    print(1)
    exit()

res = -2
l = 0

while True:
    for b in range(2**l - 1):
        m = format(b, 'b').rjust(l, '0')
        char = m.count('0') + m.count('1')*3 + l-1
        char *= src.count(chars.pop())
        res += 3 + char
        if len(chars) == 0:
            print(res)
            exit()
    l += 1
