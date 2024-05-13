input()
L=[int(x)for x in input().split()]
S=sorted(L)
print(sum(1 for i,n in enumerate(L)if n!=S[i]))