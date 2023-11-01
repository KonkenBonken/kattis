# Groups 1, 2, 3, 4 & 5:
from collections import deque

R = int(input())
C = int(input())
U = int(input())

karta = (input() for _ in range(R))

changes = ((int(x) for x in input().split()) for _ in range(U))

tiles = [list(row) for row in karta]

sthlm_y = next(y for y, row in enumerate(tiles) if 'S' in row)
sthlm_x = tiles[sthlm_y].index('S')


def print_area():
    visited = set()
    queue = deque([(sthlm_x, sthlm_y)])
    while len(queue):
        x, y = queue.popleft()

        if (x, y) not in visited:
            if x < 0 or y < 0 or y >= len(tiles) or x >= len(tiles[0]) or tiles[y][x] == '.':
                continue
            visited.add((x, y))
            queue.extend((
                (x-1, y), (x+1, y), (x, y-1), (x, y+1)
            ))
    print(len(visited))


print_area()

for y, x in changes:
    tiles[y-1][x-1] = '#'
    print_area()
