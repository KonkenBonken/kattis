L = int(input())


def en(n):
    return n * len(str(n))


def pr(n):
    print(n)
    exit()


n = 1
e = en(n)


for p in range(100, 1, -1):
    while True:
        t = n + n//p + 1
        if en(t) > L:
            break
        n = t
        e = en(n)
    if L-e < 100:
        break

while True:
    e = en(n)
    if e == L:
        pr(n)
    else:
        n += 1
