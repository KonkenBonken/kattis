N = int(input())
bags = []

for _ in range(N):
    k, *c = (int(x) for x in input().split())
    bags.append(tuple(c[2*i:2*i+2] for i in range(k)))

combinations = []


def flatten(l):
    flat = []
    for bag in l:
        flat.extend(bag)
    return flat

for length in range(1, N+1):
    for i in range(N-length+1):
        comb = flatten(flatten([[s]*n for s, n in bag]
                               for bag in bags[i:i+length]))
        combinations.append(comb)
