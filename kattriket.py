N = int(input())
States = [[]]*N
Roads = [(int(n) for n in input().split()) for _ in range(N - 1)]

for a, b in Roads:
    States[a].append(b)
    States[b].append(a)

print(States)

res = ''
tree = States[0].copy()


def branch(options, path, depth):
    print(options, path, depth)
    # return [branch([state for state in States[path[-1]] if state not in path], (*path, i), depth-1) for i, option in enumerate(options)] if

    #   for i, option in enumerate(options):
    #   options[i] = [r for r in States[state_idx] if r not in options]
    #   if depth > 0:
    #       branch(options[i], option, depth-1)


branch(tree, (0,), N-1)
