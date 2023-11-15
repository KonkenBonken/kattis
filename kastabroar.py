from collections import deque
hill_count, bridge_count = (int(x) for x in input().split())
hills = [(i, []) for i in range(hill_count)]

for _ in range(bridge_count):
    a, b = (int(x)-1 for x in input().split())
    hills[a][1].append(b)
    hills[b][1].append(a)

hills = [(i, tuple(hill)) for i, hill in hills]
unnecessary_bridges = []


def bfs(start: "tuple[int, tuple[int]]"):
    visited = set()
    queue = deque([start])
    last = -1
    while len(queue) > 0:
        hill = queue.popleft()
        if hill[0] not in visited:
            visited.add(hill[0])
            for i in hill[1]:
                if i in visited:
                    if i != last:
                        unnecessary_bridges.append((hill[0], i))
                else:
                    queue.append(hills[i])
            last = hill[0]
    return tuple(visited)


visited, clusters = [], []

for hill in hills:
    if hill[0] not in visited:
        cluster = bfs(hill)
        clusters.append(cluster)
        visited.extend(cluster)

if len(clusters)-1 <= len(unnecessary_bridges):
    print('Ja')
    print(len(clusters)-1)
    for i in range(len(clusters)-1):
        print(*[i+1 for i in (*unnecessary_bridges[i],
              clusters[i][0], clusters[i+1][0])])
else:
    print('Nej')
