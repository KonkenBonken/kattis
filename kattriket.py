N = int(input())
States = [[]for _ in range(N)]
Roads = [tuple(int(n) for n in input().split()) for _ in range(N - 1)]

for a, b in Roads:
    States[a].append(b)


def branch(roads):
    path = {}
    for state in roads:
        if len(States[state]) > 0:
            path[state] = branch(States[state])
        else:
            path[state] = None
    return path
