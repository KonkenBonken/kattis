input()
N = int(input())

houses = [(*(int(n) for n in input().split()), i) for i in range(N)]


def dist_houses(a, b=(0, 0)):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def dist(houses):
    return sum(dist_houses(houses[i], houses[i+1]) for i in range(len(houses) - 1))


houses.sort(key=dist_houses)

current = (1e9, [(0, 0, i+1) for i in range(N//2)])

for start in range(N//2):
    d = dist(houses[start:N//2+start])
    print(current[0], d)
    if d < current[0]:
        current = (d, houses[start:N//2+start])

print(" ".join(str(house[2]) for house in current[1]))
