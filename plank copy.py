N, K = (int(n) for n in input().split())
H = tuple(sorted(int(n) for n in input().split()))


def area(height):
    k = K
    h = (*H,)
    tomb = []
    print('K', k)
    for i in range(N-1, -1, -1):
        if h[i] < height:
            k -= 1
            print('k', k)
            if k < 0:
                tomb.append(h[i])
    h = (*filter(lambda l: l not in tomb, h),)
    print(height,  h)
    return height * len(h)


res = area(H[0])
for height in range(H[0] + 1, H[-1]+1):
    val = area(height)
    print('try', height, val)
    if val > res:
        res = val

print(res)
