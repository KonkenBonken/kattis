N, Q = (int(x) for x in input().split())
A = sorted(int(x) for x in input().split())
B = (int(x) for x in input().split())

for b in B:
    print(sum(A[:b]))
