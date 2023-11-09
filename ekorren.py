from collections import deque

node_count, nut_count = (int(x) for x in input().split())
nut_locations = [int(x)-1 for x in input().split()]

tree = [(i, []) for i in range(node_count)]

for _ in range(node_count-1):
    a, b = (int(x)-1 for x in input().split())
    tree[a][1].append(b)
    tree[b][1].append(a)

curr = tree[0]
dist = 0
while len(nut_locations) > 0:
    queue = deque([curr])
    while len(queue) > 0:
        node = queue.popleft()
        if node[0] in nut_locations:
            del nut_locations[nut_locations.index(node[0])]
            curr = node
            break
        queue.extend(tree[i] for i in node[1])
