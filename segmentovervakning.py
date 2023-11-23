Min, Max = (int(x) for x in input().split())
Q = int(input())

cams = dict()
last1 = False

for _ in range(Q):
    sign, *n = input().split()
    n = tuple(int(x) for x in n)

    if sign == '+':
        s, a, b = n
        cams[s] = (a, b)
    else:
        del cams[n[0]]

    if last1 in cams.values():
        print(1)
        continue

    for a, b in cams.values():
        if a <= Min and b >= Max:
            print(1)
            last1 = (a, b)
            break
    else:
        last1 = False
        for a, b in cams.values():
            for c, d in cams.values():
                if (a, b) != (c, d):
                    if b >= c and d >= a:
                        if min(a, c) <= Min and max(b, d) >= Max:
                            print(2)
                            break
            else:
                continue
            break
        else:
            print(-1)
