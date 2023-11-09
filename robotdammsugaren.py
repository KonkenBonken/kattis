R, _, _ = (int(x) for x in input().split())
sequence = input()
room = [input() for _ in range(R)]

ry = next(i for i, row in enumerate(room) if 'O' in row)
rx = next(i for i, tile in enumerate(room[ry]) if 'O' == tile)

for com in sequence:
    if com == '>':
        for i,  tile in enumerate(room[ry][rx:]):
            if '#' == tile:
                rx += i-1
                break
    elif com == '<':
        for i, tile in reversed(list(enumerate(room[ry][:rx+1]))):
            if '#' == tile:
                rx = i+1
                break
    elif com == 'v':
        for i, row in enumerate(room[ry:]):
            if '#' == row[rx]:
                ry += i-1
                break
    elif com == '^':
        for i, row in reversed(list(enumerate(room[:ry+1]))):
            if '#' == row[rx]:
                ry = i+1
                break
