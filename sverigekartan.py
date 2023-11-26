from collections import deque

R = int(input())
C = int(input())
U = int(input())

tiles = tuple(list(row) for row in (input() for _ in range(R)))
changes = ((int(x) for x in input().split()) for _ in range(U))


sthlm_y = next(y for y, row in enumerate(tiles) if 'S' in row)
sthlm_x = tiles[sthlm_y].index('S')


def adjacent(x, y):
    return filter(
        lambda c: c[0] >= 0 and c[1] >= 0 and c[1] < R and c[0] < C,
        ((x-1, y), (x+1, y), (x, y-1), (x, y+1))
    )


def print_area(mainland=set(), cx=sthlm_x, cy=sthlm_y):
    visited = mainland
    queue = deque([(cx, cy)])
    while len(queue):
        x, y = queue.popleft()

        if (x, y) not in visited:
            if tiles[y][x] == '.':
                continue
            visited.add((x, y))
            queue.extend(adjacent(x, y))

    print(len(visited))
    return visited


mainland = print_area()

for y, x in changes:
    tiles[y-1][x-1] = '#'
    adj = adjacent(x-1, y-1)

    any_mainland = any((x, y) in mainland for x, y in adj)

    if any_mainland:
        mainland = print_area(mainland, x-1, y-1)
    else:
        print(len(mainland))
