board = list(tuple(int(n) for n in input().split()) for _ in range(4))
dir = int(input())

for _ in range(4 - dir):
    board = list(zip(*board[::-1]))

for r, row in enumerate(board):
    row = list(n for n in row if n != 0)
    for i in range(len(row) - 1):
        if row[i] == row[i + 1]:
            row[i] *= 2
            row[i + 1] = 0
    row = tuple(n for n in row if n != 0)
    row += tuple(0 for _ in range(4 - len(row)))

    board[r] = row

for _ in range(dir):
    board = list(zip(*board[::-1]))

for row in board:
    print(*row)
