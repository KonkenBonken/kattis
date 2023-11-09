def nxt(i):
    for j in range(len(chairs)-i-1):
        if chairs[j+i+1] == '.':
            return j
    return 10**7


input()
chairs = input()

print(min(nxt(i) for i in range(len(chairs)) if chairs[i] == '.'))
