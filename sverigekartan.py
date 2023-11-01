# Groups 1, 2, 3 & 5:
R = int(input())
C = int(input())
U = int(input())

karta = (input() for _ in range(R))

changes = ((int(x) for x in input().split()) for _ in range(U))

tiles = [list(row) for row in karta]

sthlm_y = next(y for y, row in enumerate(tiles) if 'S' in row)
sthlm_x = tiles[sthlm_y].index('S')


def is_reachable(tile_x, tile_y):
    visited = set()

    def bfs(x, y):
        if x < 0 or y < 0 or x >= len(tiles[0]) or y >= len(tiles):
            return False
        if x == sthlm_x and y == sthlm_y:
            return True
        if tiles[y][x] == '.' or (x, y) in visited:
            return False

        visited.add((x, y))

        return bfs(x-1, y) or bfs(x+1, y) or bfs(x, y-1) or bfs(x, y+1)

    return bfs(tile_x, tile_y)


def print_area():
    area = 1
    for y, row in enumerate(tiles):
        for x, tile in enumerate(row):
            if tile == '#' and is_reachable(x, y):
                area += 1
    print(area)


print_area()

for y, x in changes:
    tiles[y-1][x-1] = '#'
    print_area()
