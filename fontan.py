N, M = (int(x) for x in input().split())
grid = [list(input()) for _ in range(N)]


def inGrid(y: int, x: int):
    return 0 <= x and x < M and 0 <= y and y < N


while True:
    prev = [row.copy() for row in grid]
    for y in range(N):
        for x in range(M):
            if prev[y][x] == 'V':
                if inGrid(y+1, x):
                    if prev[y+1][x] == '.':
                        grid[y+1][x] = 'V'

                    elif prev[y+1][x] == '#':
                        if inGrid(y, x+1) and grid[y][x+1] == '.':
                            grid[y][x+1] = 'V'

                        if inGrid(y, x-1) and grid[y][x-1] == '.':
                            grid[y][x-1] = 'V'

    if ''.join(''.join(row) for row in prev) == ''.join(''.join(row) for row in grid):
        break

print(*(''.join(row) for row in grid), sep='\n')
