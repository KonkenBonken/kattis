N = int(input())
houses = tuple([] for _ in range(N))

for _ in range(N-1):
    a, b = (int(x)-1 for x in input().split())
    print(a)
    houses[a].append(b)
