# Group 2:
R = int(input())  # = 1
C = int(input())
U = int(input())  # = 0

karta = list(input() for _ in range(R))[0]
changes = (((int(x), int(y)) for y, x in input().split()) for _ in range(R))

print(len(next(seq for seq in karta.split('.') if 'S' in seq)))
