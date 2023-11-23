from sys import setrecursionlimit
setrecursionlimit(10**6)

input()
T = input()
proteins = [input() for _ in range(int(input()))]


def r(a: str, level: int):
    if a not in T:
        return

    print(a)
    if a == T:
        print(level)
        exit()

    for b in proteins:
        r(a+b, level+1)
        r(b+a, level+1)


for a in proteins:
    r(a, 0)
