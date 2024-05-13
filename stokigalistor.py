input()
L = [int(x) for x in input().split()]
S = sorted(L)
count = 0

for i, n in enumerate(L):
    if n != S[i]:
        count += 1

print(count)
