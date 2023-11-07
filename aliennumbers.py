for case in range(int(input())):
    ali, src, trg = input().split()
    res = ''

    num = sum(src.index(c) * len(src)**i for i, c in enumerate(reversed(ali)))
    strt = next(i for i in range(10**10) if num < len(trg)**i)
        
    for i in range(strt-1, -1, -1):
        div, num = divmod(num, len(trg)**i)
        res += trg[div]

    print(f'Case #{case+1}: {res}')
