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
        lambda state: state in occupied, States[occupied[-1]]
    ))
    return tuple(step((*occupied, state)) for state in available) if len(available) > 0 else -1


print(step((0,)))
