while True:
    N, M = (int(x) for x in input().split())
    if N == 0 and M == 0:
        break
    jack, jill = 0, 0
    for _ in range(N):
        jack += 1 << int(input())
    for _ in range(N):
        jill += 1 << int(input())

    union = jack & jill
    print(sum(
        1 for i in range(union.bit_length())
        if union & 1 << i
    ))
