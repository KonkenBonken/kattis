from sys import stdin

while True:
    N, M = (int(x) for x in stdin.readline().split())
    if N == 0 and M == 0:
        break
    jack = [int(stdin.readline()) for _ in range(N)]
    jill = [int(stdin.readline()) for _ in range(M)]

    CDs, i, j = 0, 0, 0
    while i < N and j < M:
        a, b = jack[i], jill[j]
        if a < b:
            i += 1
        elif a > b:
            j += 1
        else:
            i += 1
            j += 1
            CDs += 1
    print(CDs)
