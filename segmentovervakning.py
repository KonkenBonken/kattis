Min, Max = (int(x) for x in input().split())
Q = int(input())

cams = dict()
last1, last2 = False, False

for _ in range(Q):
    sign, *n = input().split()
    n = tuple(int(x) for x in n)

    if sign == '+':
        s, a, b = n
        cams[s] = (a, b)
    else:
        del cams[n[0]]

    if last1 in cams:
        print(1)
        continue

    items = cams.items()

    for s, (a, b) in items:
        if a <= Min and b >= Max:
            print(1)
            last1 = s
            last2 = False
            break
    else:
        last1 = False
        if last2 and last2[0] in cams and last2[1] in cams:
            print(2)
            continue
        for i, (s1, (a, b)) in enumerate(items):
            for s2, (c, d) in [*items][i+1:]:
                if (a, b) != (c, d) and b >= c and d >= a and \
                        min(a, c) <= Min and max(b, d) >= Max:
                    print(2)
                    last2 = (s1, s2)
                    break
            else:
                continue
            break
        else:
            print(-1)
            last2 = False
