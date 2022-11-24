from time import time
from random import shuffle
start_time = time()

T = int(input())
N = int(input())

houses = [(*(int(n) for n in input().split()), i) for i in range(N)]


def dist(houses):
    res = 0
    for i in range(len(houses) - 1):
        res += abs(houses[i][0] - houses[i + 1][0]) + \
            abs(houses[i][1] - houses[i + 1][1])
    return res


current = (1e9, [])

while time() - 11.9 < start_time:
    shuffle(houses)
    d = dist(houses[:N//2])
    if d < current[0]:
        current = (d, houses[:N//2])


print(" ".join(str(house[2]) for house in current[1]))
