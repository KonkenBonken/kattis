# NOT SOLVED

N = int(input())
bags = []

for _ in range(N):
    k, *c = (int(x) for x in input().split())
    bags.append(tuple(c[2*i:2*i+2] for i in range(k)))

combinations = []


def flatten(l):
    flat = []
    for comb in l:
        for bag in comb:
            flat.extend(bag)
    return flat


for length in range(1, N+1):
    for i in range(N-length+1):
        comb = flatten([[s]*n for s, n in bag] for bag in bags[i:i+length])
        j = 0
        while j < len(comb):
            if comb[j] > 0 and -comb[j] in comb:
                candy = comb[j]
                del comb[j]
                if comb.index(-candy) < j:
                    j -= 1
                del comb[comb.index(-candy)]
            else:
                j += 1
        combinations.append(comb)

print(max(len(l) for l in combinations))
