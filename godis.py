N = int(input())
bags = []
for _ in range(N):
    k, *c = (int(x) for x in input().split())
    bags.append(tuple(c[2*i:2*i+2] for i in range(k)))

combinations = []

for length in range(1, N+1):
    for i in range(N-length+1):
        combinations.append(bags[i:i+length])
