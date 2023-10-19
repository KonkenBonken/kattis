N, K = (int(n) for n in input().split())
H = tuple(int(n) for n in input().split())


def area(height):
    h = (
        *tuple(p for p in H if p < height)[:max(K, 0)],
        *tuple(p for p in H if p >= height)
    )
    return len(h)*height


res = area(H[0])
for height in range(H[0] + 1, H[-1]+1):
    val = area(height)
    if val <= res:
        break
    res = val

print(res)


# 7 2
# 1 2 4 5 5 6 6
