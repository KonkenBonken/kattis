from collections import deque
hill_count, bridge_count = (int(x) for x in input().split())
hills = [(i, []) for i in range(hill_count)]

for _ in range(bridge_count):
    a, b = (int(x)-1 for x in input().split())
    hills[a][1].append(b)
    hills[b][1].append(a)

hills = [(i, tuple(hill)) for i, hill in hills]
unnecessary_bridges = set()


def bfs(start: "tuple[int, tuple[int]]"):
    visited = set()
    queue = deque([(start, -1)])
    last = -1
    while len(queue) > 0:
        hill, fr = queue.popleft()
        if hill[0] not in visited:
            visited.add(hill[0])
            for i in hill[1]:
                if i in visited:
                    if i != last:
                        unnecessary_bridges.add((hill[0], i))
                else:
                    queue.append((hills[i], hill[0]))
            last = hill[0]
    return visited


visited, clusters = [], []

for hill in hills:
    if hill[0] not in visited:
        cluster = bfs(hill)
        clusters.append(cluster)
        visited.extend(cluster)

if len(clusters)-1 <= len(unnecessary_bridges):
    print('Ja')
    print(len(clusters)-1)
else:
    print('Nej')
