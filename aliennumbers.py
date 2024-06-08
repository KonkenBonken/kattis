from math import floor, log

for case in range(int(input())):
    ali, src, trg = input().split()
    res = ''

    num = sum(src.index(c) * len(src)**i for i, c in enumerate(reversed(ali)))
    reslen = floor(log(num, len(trg))) + 1

    for i in range(reslen-1, -1, -1):
        div, num = divmod(num, len(trg)**i)
        res += trg[div]

    print(f'Case #{case+1}: {res}')
