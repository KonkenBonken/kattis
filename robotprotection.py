while True:
    N = int(input())
    if N==0:
        break
    points = tuple(tuple(int(x) for x in input().split()) for _ in range(N))
    print(points)
