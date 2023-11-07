cases = int(input())

for case in range(1, cases+1):
    ali, src, trg = input().split()
    num = 0

    for i, c in enumerate(reversed(ali)):
        num += src.index(c) * len(src)**i
    
    trg_base, res = len(trg), ''
    
    strt = next(i for i in range(10**10) if num<trg_base**i)
    for i in range(strt-1,-1,-1):
        div,mod = divmod(num,trg_base**i)
        res += trg[div]
        num = mod
        
    print(f'Case #{case}: {res}')