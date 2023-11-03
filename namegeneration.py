N = int(input())
names = set()

vw = ('a', 'e', 'i', 'o', 'u')
cn = ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm',
      'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z')


def has_3_1(n):
    a = n >> 1
    b = n & a
    c = b >> 1
    return c & b != 0


def has_3(n):
    return has_3_1(n) or has_3_1(int("{0:b}".format(n).replace('1', 'x').replace('0', '1').replace('x', '0'), 2))


def gen():
    i = 599186
    while True:
        i += 1
        if has_3(i):
            continue
        for c in range(len(cn)):
            name = ''
            for j in range(20):
                charset = cn if i & (2**j) else vw
                name += charset[c % len(charset)]
            yield name


names = gen()
print(*(next(names) for _ in range(N)), sep='\n')
