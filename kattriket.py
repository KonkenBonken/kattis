N = int(input())
States = [[]]*N
Roads = [(int(n) for n in input().split()) for _ in range(N - 1)]

for a, b in Roads:
    States[a].append(b)
    States[b].append(a)

print(States)

res = ''
tree = States[0]


def flat_map(f, xs):
    ys = []
    for x in xs:
        ys.extend(f(x))
    return ys


def branch(options):
    print('tree', tree, options)
    for i in range(2, len(options)):
        options[i] = list(States[options[i]])
        branch(options[i])


branch(tree)
print(tree)
