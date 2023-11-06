L = int(input())

for n in range(L+1):
    en = n * len(str(n))
    if en == L:
        print(n)
        break
