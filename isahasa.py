N, M = (int(x) for x in input().split())

objects = dict()

for _ in range(N):
    a, cmd, b = input().split()

    if a == b:
        continue

    if a not in objects:
        objects[a] = {'name': a, 'is-a': [], 'has-a': []}

    if b not in objects:
        objects[b] = {'name': b, 'is-a': [], 'has-a': []}

    objects[a][cmd].append(objects[b])


def isa(a, b):
    if a == b:
        return True

    for isa in objects[a]['is-a']:
        if isa['name'] == b:
            return True

        for o in isa['is-a']:
            if isa(a, o):
                return True

    return False


for i in range(1, M+1):
    a, cmd, b = input().split()

    if cmd == 'is-a':
        if isa(a, b):
            print(f'Query {i}: true')
        else:
            print(f'Query {i}: false')
