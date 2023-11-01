R = int(input())
C = int(input())
U = int(input())

karta = (input() for _ in range(R))
changes = (((int(x), int(y)) for y, x in input().split()) for _ in range(R))

for row in karta:
    print(row)
