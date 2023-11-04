N, Q = (int(n) for n in input().split())
people = list(0 for _ in range(N))

for _ in range(Q):
    instruction, *n = input().split()

    if instruction == 'SET':
        i, x = (int(m) for m in n)
        people[i-1] = x
    elif instruction == 'RESTART':
        people = list(int(n[0]) for _ in range(N))
    elif instruction == 'PRINT':
        print(people[int(n[0])-1])
