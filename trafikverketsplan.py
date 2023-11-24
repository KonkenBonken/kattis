from collections import deque

N = int(input())
houses = tuple([] for _ in range(N))

for _ in range(N-1):
    a, b = (int(x)-1 for x in input().split())
    houses[a].append(b)

for _ in range(int(input())):
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
            visited.add(house)
    else:
        print('nej')
