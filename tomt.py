input()
N = int(input())

houses = [(*(int(n) for n in input().split()), i) for i in range(N)]


def dist_houses(a, b=(0, 0)):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def dist(houses):
    return sum(dist_houses(houses[i], houses[i+1]) for i in range(len(houses) - 1))


def closest(path, i):
    house = path[i-1]
    return min((h for h in houses if h not in path), key=lambda h: dist_houses(house, h))


current = (int(1e9), [(0, 0, i+1) for i in range(N//2)])

for start in range(N):
    d = 0
    path = [None]*(N//2)
    path[0] = houses[start]
    for i in range(1, N//2):
        path[i] = closest(path, i)
        d += dist_houses(houses[start], path[i])
    if d < current[0]:
        current = (d, path)

print(" ".join(str(house[2]) for house in current[1]))
