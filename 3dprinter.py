N = int(input())

def D(statues,printers,days):
    if statues == N:
        return days
    
    return min(D(statues+(printers-new_printers),printers+new_printers,days+1) for new_printers in range(printers+1))
    
print(D(0,1,0))