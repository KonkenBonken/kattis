Min, Max = (int(x) for x in input().split())
Q = int(input())

l_cams, u_cams, f_cams = dict(), dict(), set()

for _ in range(Q):
    sign, s, *n = input().split()

    if sign == '+':
        a, b = (int(x) for x in n)
        if a <= Min and b >= Max:
            f_cams.add(s)
        elif a <= Min and b >= Min:
            l_cams[s] = b
        elif a <= Max and b >= Max:
            u_cams[s] = a
    else:
        l_cams.pop(s, 0)
        u_cams.pop(s, 0)
        f_cams.discard(s)

    if len(f_cams) != 0:
        print(1)
    elif len(l_cams) != 0 and len(u_cams) != 0:
        if max(l_cams.values()) >= min(u_cams.values()):
            print(2)
            continue
    print(-1)
