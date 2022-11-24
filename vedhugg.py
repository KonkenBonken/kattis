N, S = [int(n) for n in input().split()]
trees = [0]*N

for i in range(N):
    trees[i] = [int(n) for n in input().split()]


def wood(sec):
    return sum(tree[0] + tree[1] * min(tree[2], sec) for tree in trees)


if wood(0) >= S:
    print(0)
    quit()

k = 1

while wood(k) < S:
    k *= 2

for e in range(8, -1, -1):
    while wood(k - 10**e) >= S:
        k -= 10**e

print(int(k))
