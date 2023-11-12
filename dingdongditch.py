input()
houses = sorted(int(x) for x in input().split())

friends = sorted(((i, int(b))
                 for i, b in enumerate(input().split())), key=lambda v: v[1])

total, last = 0, 0

for i, friend in enumerate(friends):
    j, count = friend
    total += sum(houses[last:count])
    last = count
    friends[i] = j, total

print(*[x for _, x in sorted(friends, key=lambda v: v[0])], sep='\n')
