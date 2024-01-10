while True:
    N, M = (int(x) for x in input().split())
    if N == 0 and M == 0:
        break
    jack, jill = 0, 0
    for _ in range(N):
        jack += 1 << int(input())
    for _ in range(N):
        jill += 1 << int(input())

    uni = jack & jill
    print(bin(uni).count("1"))
