from collections import deque
hill_count, bridge_count = (int(x) for x in input().split())
hills = [[] for _ in range(hill_count)]

for _ in range(bridge_count):
    a, b = (int(x)-1 for x in input().split())
    print(a, b)
    hills[a].append(b)
    hills[b].append(a)

hills = [tuple(hill) for hill in hills]

def bfs(start: "list[int]"):
    visited = set()
    queue = deque([start])
    while len(queue) > 0:
        hill = queue.popleft()
        if hill not in visited:
            visited.add(hill)
            queue.extend(hills[i] for i in hill)


bfs(hills[0])
