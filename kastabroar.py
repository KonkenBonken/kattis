hill_count, bridge_count = (int(x) for x in input().split())
hills = [[] for _ in range(hill_count)]

for _ in range(bridge_count):
    a, b = (int(x)-1 for x in input().split())
    print(a, b)
    hills[a].append(b)
    hills[b].append(a)
