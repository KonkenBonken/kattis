letters = tuple('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')


def sort(name: str):
    return letters.index(name[0]) * len(letters) + letters.index(name[1])


first = True
while True:
    N = int(input())
    if N == 0:
        break

    if not first:
        print()
    first = False

    names = tuple(input() for _ in range(N))
    print(*sorted(names, key=sort), sep='\n')
