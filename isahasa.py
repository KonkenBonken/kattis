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
        print(f'Query {i}: {str(a in isa and b in isa[a]).lower()}')

    if cmd == 'has-a':
        if a in hasa and b in hasa[a]:
            print(f'Query {i}: true')

        else:
            for cls in isa[a]:
                if cls in hasa and b in hasa[cls]:
                    print(f'Query {i}: true')
                    break
            else:
                print(f'Query {i}: false')
