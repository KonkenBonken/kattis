N = int(input())
States = [[]]*N
Roads = [(int(n) for n in input().split()) for _ in range(N - 1)]

for a, b in Roads:
    States[a].append(b)
    States[b].append(a)

print(States)

res = ''
tree = States[0].copy()


def branch(options, state_idx):
    for i in range(len(options)):
        options[i] = list(States[options[i]])
        States[options[i]].remove(state_idx)  # dont burn global bridges
        States[state_idx].remove(options[i])
        branch(options[i], options[i])


branch(tree, 0)
print(tree)
