_, K = (int(x) for x in input().split())
L = [int(x) for x in input().split()]

if K == 1:
    print(1)
    exit()


revL = list(enumerate(L*2))[::-1]
two = next((j, y) for (j, y) in revL if y == 2)
start_i = next(i for i, x in revL[revL.index(two):] if x == 1)
start_i %= len(L)

k = 2
i = start_i

while k <= K:
    i += (L[i % len(L):]+L).index(k)
    k += 1

print(i-start_i+1)
