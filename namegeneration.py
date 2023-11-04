k,i,n=lambda n:((n&(n>>1))>>1)&(n&(n>>1))!=0,599184,int(input())
q,h=i+n/2,lambda n:k(n)or k(int(format(n,'b').replace(*'1x').replace(*'01').replace(*'x0'),2))
if n%2:
 print 'abc'
while i<q:
 i+=1
 if h(i):
  q+=1
 else:
  l=''.join('ab'[(i>>j)&1]for j in range(20))
  print l
  print l.replace(*'ae')