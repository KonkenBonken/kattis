R, _, _ = (int(x) for x in input().split())
sequence = input()
room = [input() for _ in range(R)]

ry = next(i for i, row in enumerate(room) if 'O' in row)
rx = next(i for i, tile in enumerate(room[ry]) if 'O' == tile)

for com in sequence:
    if com == '>':
        rx = next(i+rx-1 for i,
                  tile in enumerate(room[ry][rx:]) if '#' == tile)
    elif com == '<':
        rx = next(i+1 for i, tile in reversed(
            list(enumerate(room[ry][:rx+1]))) if '#' == tile)
    elif com == 'v':
        ry = next(i+ry-1 for i, row in enumerate(room[ry:]) if '#' == row[rx])
    elif com == '^':
        ry = next(i+1 for i, row in reversed(
            list(enumerate(room[:ry+1]))) if '#' == row[rx])
