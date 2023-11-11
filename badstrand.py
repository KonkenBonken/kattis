N, B = (int(x) for x in input().split())
A = [int(x) for x in input().split()]

for l in range(N+1, 0, -1):
    for i in range(N-l+1):
        if sum(A[i:i+l]) <= B:
            print(l)
            exit()
