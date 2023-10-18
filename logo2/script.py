from math import cos, sin, sqrt

test_count = int(input())
command_count = int(input())
raw_commands = [input().split() for _ in range(command_count)]

commands = []
missing = None

for cmd, amt in raw_commands:
    if amt == '?':
        missing = cmd
        if missing[1] == 't':
            raise 'turn'
    else:
        commands.append((cmd, int(amt)))

print(commands, missing)

x, y, θ = 0, 0, 0

for cmd, amt in commands:
    if cmd[1] == 't':
        if cmd[0] == 'l':
            amt *= -1
        θ = (θ + amt) % 360
    else:
        if cmd[0] == 'b':
            amt *= -1
        x += cos(θ) * amt
        y += sin(θ) * amt
    print(x, y, θ)

print(sqrt(x**2 + y**2))
