node_count, nut_count = (int(x) for x in input().split())
nut_locations = [int(x)-1 for x in input().split()]

tree = [(i, []) for i in range(node_count)]

for _ in range(node_count-1):
    a, b = (int(x)-1 for x in input().split())
    tree[a][1].append(b)
    tree[b][1].append(a)
