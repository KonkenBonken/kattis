Min, Max = (int(x) for x in input().split())
Q = int(input())

l_cams, u_cams, f_cams = dict(), dict(), set()

for _ in range(Q):
    sign, *n = input().split()
    n = tuple(int(x) for x in n)

    if sign == '+':
        s, a, b = n
        if a <= Min and b >= Max:
            f_cams.add(s)
        elif a <= Min and b >= Min:
            l_cams[s] = b
        elif a <= Max and b >= Max:
            u_cams[s] = a
    else:
        l_cams.pop(n[0], 0)
        u_cams.pop(n[0], 0)
        f_cams.discard(n[0])

    if len(f_cams) != 0:
        print(1)
    elif len(l_cams) != 0 and len(u_cams) != 0:
        if max(l_cams.values()) >= min(u_cams.values()):
            print(2)
            continue
    print(-1)
