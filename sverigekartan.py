R = int(input())
C = int(input())
U = int(input())

tiles = tuple(list(row) for row in (input() for _ in range(R)))
changes = ((int(x) for x in input().split()) for _ in range(U))


sthlm_y = next(y for y, row in enumerate(tiles) if 'S' in row)
sthlm_x = tiles[sthlm_y].index('S')


def adjacent(x, y):
    return filter(
        lambda c: c[0] >= 0 and c[1] >= 0 and c[1] < len(
            tiles) and c[0] < len(tiles[0]),
        ((x-1, y), (x+1, y), (x, y-1), (x, y+1))
    )


def print_area():
    visited = set()
    queue = [(sthlm_x, sthlm_y)]
    padLeft = 0
    while padLeft < len(queue):
        x, y = queue[padLeft]
        padLeft += 1

        if (x, y) not in visited:
            if tiles[y][x] == '.':
                continue
            visited.add((x, y))
            queue.extend(adjacent(x, y))

    print(len(visited))


print_area()

for y, x in changes:
    tiles[y-1][x-1] = '#'
    print_area()
