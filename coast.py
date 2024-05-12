from collections import deque

H, W = map(int, input().split())

grid: 'list[tuple[bool,int,int]]' = []

for y in range(H):
    grid.extend((n == '1', x, y) for x, n in enumerate(input()))


def at(x: int, y: int):
    if x >= 0 and x < W and y >= 0 and y < H:
        return grid[x+y*W]


def neighbors(tile):
    _, x, y = tile
    return (t for t in [
        at(x+1, y),
        at(x, y+1),
        at(x-1, y),
        at(x, y-1),
    ] if t)


if W == 1 or H == 1:
    p = grid[0][0]
    coast = 0
    if p:
        coast += 3
    for l, _, _ in grid[1:]:
        if p != l:
            coast += 1
        if l:
            coast += 2
        p = l
    if p:
        coast += 1
    print(coast)
    exit()

if W == 2 or H == 2:
    if H > W:
        grid = [a[0] for a in zip(grid[::-1])]
        H, W = W, H

    p = grid[0][0]
    coast = 0
    if p:
        coast += 2
    if grid[W-1][0]:
        coast += 1

    for l, _, _ in grid[1:W]:
        if p != l:
            coast += 1
        if l:
            coast += 1
        p = l

    p = grid[W][0]
    if p:
        coast += 2
    if grid[-1][0]:
        coast += 1
    if grid[0][0] != p:
        coast += 1

    for i, t in enumerate(grid[W+1:]):
        l = t[0]
        if p != l:
            coast += 1
        if l:
            coast += 1
        if grid[i+1][0] != l:
            coast += 1
        p = l

    print(coast)
    exit()

queue = deque((l, x, y) for l, x, y in grid
              if not l and (y == 0 or y == H-1 or x == 0 or x == W-1))

coast = H*2 + W*2 - 4 - len(queue)
visited = set(queue)

while len(queue):
    tile = queue.popleft()
    neighs = neighbors(tile)
    for n in neighs:
        if n[0]:
            coast += 1
        else:
            if n not in visited:
                queue.append(n)
                visited.add(n)

print(coast)
