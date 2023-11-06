L = int(input())

def en(n):
    return n * len(str(n))

n = 2**20
e=-1

for _ in range(50):
    e = en(n)
    if e == L:
        print(n)
        break
    elif e > L:
        n //= 2
    elif e < L:
        n = n + n//2
else:
    while True:
        e = en(n)
        if e == L:
            print(n)
            break
        elif e > L:
            n -= 1
        elif e < L:
            n += 1
