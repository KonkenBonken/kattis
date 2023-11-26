Min, Max = (int(x) for x in input().split())
Q = int(input())

l_cams, u_cams, f_cams = dict(), dict(), set()
l_max, u_min = 0, 10**9
l_chg, u_chg = False, False

for _ in range(Q):
    sign, s, *n = input().split()

    if sign == '+':
        a, b = (int(x) for x in n)
        if a <= Min and b >= Max:
            f_cams.add(s)
        elif a <= Min and b >= Min:
            l_cams[s] = b
            l_chg = True
        elif a <= Max and b >= Max:
            u_cams[s] = a
            u_chg = True
    else:
        if l_cams.pop(s, -1) == -1:
            if u_cams.pop(s, -1) == -1:
                f_cams.discard(s)
            else:
                u_chg = True
        else:
            l_chg = True

    if len(f_cams) != 0:
        print(1)
        continue
    elif len(l_cams) == 0 or len(u_cams) == 0:
        print(-1)
        continue

    if l_chg:
        l_max = max(l_cams.values())
    if u_chg:
        u_min = min(u_cams.values())

    if l_max >= u_min:
        print(2)
    else:
        print(-1)
