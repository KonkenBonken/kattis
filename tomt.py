from time import time
from random import shuffle
start_time = time()

input()
N = int(input())

houses = [(*(int(n) for n in input().split()), i) for i in range(N)]


def dist_houses(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def dist(houses):
    return sum(dist_houses(houses[i], houses[i+1]) for i in range(len(houses) - 1))


current = (1e9, [(0, 0, i+1) for i in range(N//2)])

while time() - 11.9 < start_time:
    shuffle(houses)
    for start in range(N//2):
        d = dist(houses[start:N//2+start])
        if d < current[0]:
            current = (d, houses[start:N//2+start])
    houses.reverse()
    for start in range(N//2):
        d = dist(houses[start:N//2+start])
        if d < current[0]:
            current = (d, houses[start:N//2+start])


print(" ".join(str(house[2]) for house in current[1]))
