while True:
    N, M = (int(x) for x in input().split())
    if N == 0 and M == 0:
        break
    jack = set(input() for _ in range(N))
    jill = (input() for _ in range(M))
    CDs = 0
    for cd in jill:
        if cd in jack:
            CDs += 1
    print(CDs)
