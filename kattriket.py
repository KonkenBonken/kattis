N = int(input())
States = [[] for _ in range(N)]
Roads = [tuple(int(n) for n in input().split()) for _ in range(N - 1)]

for road in Roads:
    States[min(road)].append(max(road))

res = [1]


def branch(roads):
    path = []
    for state in roads:
        if len(States[state]) > 0:
            path.append(branch(States[state]))
        else:
            path.append(None)
    return path


tree = branch(States[0])
levels = [len(tree)]


def level(tree):
    levels.append(sum(len(obj) for obj in tree if isinstance(obj, list)))
    for branch in tree:
        if isinstance(branch, list):
            level(branch)


level(tree)
del levels[levels.index(0):]

n = 1
for l in levels:
    res.append(n)
    for _ in range(l-1):
        n += 1
        res.append(n)

del res[-1]
print(' ' .join(map(str, res)))
