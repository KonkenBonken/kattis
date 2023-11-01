# Group 2 & 3:
R = int(input())  # = 1
C = int(input())
U = int(input())

karta = next(input() for _ in range(R))

changes = ((int(x) for x in input().split()) for _ in range(U))

tiles = list(karta)


def print_area():
    print(len(next(seq for seq in "".join(tiles).split('.') if 'S' in seq)))


print_area()

for _, x in changes:
    tiles[x-1] = '#'
    print_area()
