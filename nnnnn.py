L = int(input())

for t in range(L):
    en = str(t) * t
    if len(en) == L:
        print(t)