from collections import deque

N = int(input())
houses = tuple([] for _ in range(N))

for _ in range(N-1):
    a, b = (int(x)-1 for x in input().split())
    houses[a].append(b)

Q = int(input())

for _ in range(Q):
    h, w = (int(x)-1 for x in input().split())

    queue = deque([h])
    visited = set()
    while len(queue) > 0:
        house = queue.popleft()
        if house == w:
            print('ja')
            break
        if house not in visited:
            queue.extend(houses[house])
    else:
        print('nej')
