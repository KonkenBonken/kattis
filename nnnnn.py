from math import ceil


L = int(input())


def en(n):
    return n * len(str(n))


def pr(n):
    print(n)
    exit()


n = 10**20
global e
e = -1


for p in range(100, 1, -1):
    e = en(n)

    if e > L:
        while e > L:
            n //= p
            e = en(n)
    elif e < L:
        while e < L:
            n = n + ceil(n/p)
            e = en(n)
    else:
        pr(n)

while True:
    e = en(n)
    if e == L:
        pr(n)
    else:
        n += -1 if e > L else 1
