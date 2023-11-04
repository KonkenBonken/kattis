k,i,n=lambda n:((b:=n&(n>>1))>>1)&b!=0,599184,int(input())
q,r,h=i+n,range(20),lambda n:k(n)or k(int(format(n,'b').replace(*'1x').replace(*'01').replace(*'x0'),2))
while i<q:
    i+=1
    if h(i):
        q+=1
    else:
        print(''.join('ab'[(i>>j)&1]for j in r))