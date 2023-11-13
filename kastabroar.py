from collections import deque
hill_count, bridge_count = (int(x) for x in input().split())
hills = [(i, []) for i in range(hill_count)]

for _ in range(bridge_count):
    a, b = (int(x)-1 for x in input().split())
    hills[a][1].append(b)
    hills[b][1].append(a)

hills = [(i, tuple(hill)) for i, hill in hills]


def bfs(start: "tuple[int, tuple[int]]"):
    visited = set()
    queue = deque([start])
    while len(queue) > 0:
        hill = queue.popleft()
        if hill[0] not in visited:
            visited.add(hill[0])
            queue.extend(hills[i] for i in hill[1])


bfs(hills[0])
