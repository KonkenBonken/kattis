from collections import deque

N = int(input())
houses = tuple(list() for _ in range(N))

for _ in range(N-1):
    a, b = (int(x)-1 for x in input().split())
    houses[a].append(houses[b])

for _ in range(int(input())):
    h, w = (houses[int(x)-1] for x in input().split())

    queue = deque([h])
    while len(queue) > 0:
        house = queue.popleft()
        if house is w:
            print('ja')
            break
        queue.extend(house)
        h.extend(house)
    else:
        print('nej')
