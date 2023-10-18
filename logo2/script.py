from math import cos, sin, sqrt

test_count = int(input())
command_count = int(input())
raw_commands = [input().split() for _ in range(command_count)]

missing_index = next(i for i in range(command_count) if raw_commands[i][-1] == '?')

missing_command = raw_commands[missing_index][0]
first_half = [(cmd,int(amt)) for cmd,amt in raw_commands[:missing_index]]
second_half = [(cmd,int(amt)) for cmd,amt in raw_commands[missing_index + 1:]]


fx, fy, θ = 0, 0, 0

for cmd, amt in first_half:
    if cmd[1] == 't':
        if cmd[0] == 'l':
            amt *= -1
        θ = (θ + amt) % 360
    else:
        if cmd[0] == 'b':
            amt *= -1
        fx += cos(θ) * amt
        fy += sin(θ) * amt
print(fx, fy, θ)

sx, sy, θ = 0, 0, 0

for cmd, amt in reversed(second_half):
    if cmd[1] == 't':
        if cmd[0] == 'r':
            amt *= -1
        θ = (θ + amt) % 360
    else:
        if cmd[0] == 'f':
            amt *= -1
        sx += cos(θ) * amt
        sy += sin(θ) * amt
print(sx, sy, θ)

print(sqrt((fx-sx)**2+(fy-sy)**2))