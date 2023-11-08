def F(n):
    if n <= 1:
        return str(n)
    a, b = 1, 2
    for _ in range(n-2):
        c = b << a.bit_length() | a
        a, b = b, c
    return format(b, 'b')


i = 1
while True:
    try:
        n, p = int(input()), input()
        f, o = F(n), 0
        for c in range(len(f) - len(p) + 1):
            if f[c:c+len(p)] == p:
                o += 1
        print(f'Case {i}: {o}')
        i += 1
    except EOFError:
        break
