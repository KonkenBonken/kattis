N = int(input())

if N == 1:
    print(1)
else:
    last = 10**5
    for printers in range(1, N+1):
        days, statues = printers-1, 0
        while statues < N:
            days += 1
            statues += printers
        
        if days >= last:
            print(last)
            break
        
        last = days
        printers+=1