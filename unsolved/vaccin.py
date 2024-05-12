# NOT SOLVED

input()
days = [int(x) for x in input().split()]
people = sorted(enumerate(int(x) for x in input().split()), key=lambda v: v[1])
res = []

for j, person in enumerate(people):
    pi, queue = person
    queue += 1
    for i, vaccins in enumerate(days):
        queue -= vaccins
        if queue <= 0:
            res.append((pi, i+1))
            break
    else:
        res.append((pi, -1))

print(*[val for _, val in sorted(res, key=lambda v: v[0])], sep='\n')
