def F(n):
    if n <= 1:
        return n
    a, b = 1, 2
    for _ in range(n-2):
        c = b << a.bit_length() | a
        a, b = b, c
    return b


i = 1
while True:
    try:
        n, p = int(input()), int(input(), 2)
        f, o = F(n), 0
        for c in range(f.bit_length() - p.bit_length() + 1):
            if f & p << c == p << c:
                o += 1
        print(f'Case {i}: {o}')
        i += 1
    except EOFError:
        break
