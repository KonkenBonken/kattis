from collections import deque

N = int(input())
houses = tuple(set() for _ in range(N))

for _ in range(N-1):
    a, b = (int(x)-1 for x in input().split())
    houses[a].add(b)

for h in range(N):
    queue = deque([h])
    while len(queue) > 0:
        house = queue.popleft()
        queue.extend(houses[house])
        houses[h].update(houses[house])

for _ in range(int(input())):
    h, w = (int(x)-1 for x in input().split())
    if h == w:
        print('ja')
    else:
        print('ja' if w in houses[h] else 'nej')
