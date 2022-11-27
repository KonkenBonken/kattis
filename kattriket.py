N = int(input())
States = [[] for _ in range(N)]
Roads = [tuple(int(n) for n in input().split()) for _ in range(N - 1)]

for a, b in Roads:
    States[a].append(b)
    States[b].append(a)

res = [1]
if len(States[0]) % 2 == 1:
    res.append(1)


def branch(roads, prev):
    path = []
    for state in roads:
        if (state not in prev) and len(States[state]) > 0:
            path.append(branch(States[state], (*prev, state)))
        else:
            path.append(None)
    return path


tree = branch(States[0], (0,))
levels = [len(tree)]


def level(tree):
    levels.append(sum(len(obj) for obj in tree if isinstance(obj, list)))
    for branch in tree:
        if isinstance(branch, list):
            level(branch)


level(tree)

n = 1
for l in levels:
    if len(res) >= N-1:
        break
    res.append(n)
    for _ in range(l-1):
        n += 1
        res.append(n)

del res[N-1:]
print(' ' .join(map(str, res)))
