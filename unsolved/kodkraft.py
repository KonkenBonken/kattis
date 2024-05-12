# NOT SOLVED

_, K = (int(x) for x in input().split())
L = [int(x) for x in input().split()]

if K == 1:
    print(1)
    exit()


def lasti(l, v, s):
    return next(i for i in reversed(range(len(l)-s)) if l[i] == v)


answer = 10**7

two_indexes = (i for i, x in enumerate(L) if x == 2)

for two_i in two_indexes:
    start_i = lasti(L*2, 1, two_i + len(L)) % len(L)

    k = 2
    i = start_i

    while k <= K:
        i += (L[i % len(L):] + L).index(k)
        k += 1

    answer = min(answer, i-start_i+1)

print(answer)
