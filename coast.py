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


queue = deque((l, x, y) for l, x, y in grid
              if not l and (y == 0 or y == H-1 or x == 0 or x == W-1))

coast = H*2 + W*2 - 4 - len(queue)
visited = set(queue)

visual = [[0 for x in range(W)] for y in range(H)]

while len(queue):
    tile = queue.popleft()
    neighs = neighbors(tile)
    print(tile, tuple(neighbors(tile)))
    for n in neighs:
        if n[0]:
            coast += 1
            visual[tile[2]][tile[1]] += 1
            print(coast)
        else:
            if n not in visited:
                queue.append(n)
                visited.add(n)

print(*visual, sep='\n')

print(coast)
