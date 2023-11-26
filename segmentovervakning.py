# Group 1-4

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
            l_max = max(l_max, b)
        elif a <= Max and b >= Max:
            u_cams[s] = a
            u_min = min(u_min, a)
    else:
        if l_cams.pop(s, -1) == -1:
            if u_cams.pop(s, -1) == -1:
                f_cams.discard(s)
            else:
                u_min = min([*u_cams.values(), 10**9])
        else:
            l_max = max([*l_cams.values(), 0])

    if len(f_cams) != 0:
        print(1)
        continue
    elif len(l_cams) == 0 or len(u_cams) == 0:
        print(-1)
        continue

    if l_max >= u_min:
        print(2)
    else:
        print(-1)
