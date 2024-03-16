N, M = (int(x) for x in input().split())

isa, hasa = dict(), dict()

for _ in range(N):
    a, cmd, b = input().split()
    if cmd == 'is-a':
        if a not in isa:
            isa[a] = [a]
        isa[a].append(b)

    if cmd == 'has-a':
        if a not in hasa:
            hasa[a] = [a]
        hasa[a].append(b)

for i in range(1, M+1):
    a, cmd, b = input().split()
    if cmd == 'is-a':
        print(f'Query {i}: {a in isa and b in isa[a]}')

    if cmd == 'has-a':
        print(f'Query {i}: {a in hasa and b in hasa[a]}')
