# NOT SOLVED

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


def isaMemo(a, b):
    objects[a]['is-a'].insert(0, {'name': b, 'is-a': [], 'has-a': []})


def isa(a, b):
    if a == b:
        return True

    for obj in objects[a]['is-a']:
        if obj['name'] == b:
            isaMemo(a, b)
            return True

        for o in obj['is-a']:
            isaMemo(a, b)
            if isa(a, o['name']):
                return True

    return False


def hasa(a, b):
    if a == b:
        return False

    for obj in objects[a]['has-a']:
        if obj['name'] == b:
            return True

        for o in obj['is-a']:
            if o['name'] == b:
                return True

    for obj in objects[a]['is-a']:
        for o in obj['is-a']:
            if o['name'] == b:
                return True

        if isa(a, obj['name']):
            return True

    return False


for i in range(1, M+1):
    a, cmd, b = input().split()

    if cmd == 'is-a':
        if isa(a, b):
            print(f'Query {i}: true')
        else:
            print(f'Query {i}: false')

    elif cmd == 'has-a':
        if hasa(a, b):
            print(f'Query {i}: true')
        else:
            print(f'Query {i}: false')
