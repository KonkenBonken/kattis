N = int(input())
States = ([],)*N
Roads = [(int(n) for n in input().split()) for _ in range(N - 1)]

for a, b in Roads:
    States[a].append(b)
    States[b].append(a)

print(States)

res = ''


def step(occupied):
    available = tuple(filter(
        lambda state: state not in occupied, States[occupied[-1]]
    ))
    if len(available) > 1:
        return tuple(step((*occupied, state)) for state in available)
    else:
        return available[0]


print(step((0,)))
