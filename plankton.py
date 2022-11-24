A = int(input())
input()
l  = [int(n) for n in input().split()]
res = 0

l.sort()
    
while len(l) > 1:
    if l[0] * l[-1] >= A:
        res += 1
        del l[-1]
    del l[0]

print(res)