R, _, _ = (int(x) for x in input().split())
sequence = input()
room = [input() for _ in range(R)]

ry = next(i for i, row in enumerate(room) if 'O' in row)
rx = next(i for i, tile in enumerate(room[ry]) if 'O' == tile)
