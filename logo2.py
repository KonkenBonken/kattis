from math import cos, sin, radians as rad, degrees as deg

test_count = int(input())
command_count = int(input())
raw_commands = [input().split() for _ in range(command_count)]

missing_index = next(i for i in range(command_count)
                     if raw_commands[i][-1] == '?')

missing_command = raw_commands[missing_index][0]
first_half = [(cmd, int(amt)) for cmd, amt in
              raw_commands[:missing_index]]
second_half = [(cmd, int(amt)) for cmd, amt in
               raw_commands[missing_index + 1:]]


fx, fy, fθ = 0, 0, 0

for cmd, amt in first_half:
    if cmd[1] == 't':
        if cmd[0] == 'l':
            amt *= -1
        fθ = (fθ + rad(amt)) % rad(360)
    else:
        if cmd[0] == 'b':
            amt *= -1
        fx += cos(fθ) * amt
        fy += sin(fθ) * amt

sx, sy, sθ = 0, 0, fθ

for cmd, amt in second_half:
    if cmd[1] == 't':
        if cmd[0] == 'l':
            amt *= -1
        sθ = (sθ + rad(amt)) % rad(360)
    else:
        if cmd[0] == 'b':
            amt *= -1
        sx += cos(sθ) * amt
        sy += sin(sθ) * amt

if missing_command[1] == 't':
    m = -1 if missing_command[0] == 'r' else 1
    print(round(360 - deg(sθ))*m % 360)

else:
    m = -1 if missing_command[0] == 'b' else 1
    step = 1
    while True:
        fx += cos(fθ)*m
        fy += sin(fθ)*m

        rx = fx + sx
        ry = fy + sy
        
        if abs(rx) < .005 and abs(ry) < .005:
            print(step)
            break

        step += 1
