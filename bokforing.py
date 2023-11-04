N, Q = (int(n) for n in input().split())
base, people = 0, {}

for _ in range(Q):
    instruction, *n = input().split()

    if instruction == 'SET':
        i, x = (int(m) for m in n)
        people[i] = x
    elif instruction == 'RESTART':
        base, people = int(n[0]), {}
    elif instruction == 'PRINT':
        print(people.get(int(n[0]), base))
