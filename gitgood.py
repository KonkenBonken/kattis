N = int(input())
path = []
prints = set()

for _ in range(N):
    cmd = input()

    if cmd.startswith('cd '):
        cmd = cmd[3:]
        if cmd == '..':
            del path[-1]
        else:
            path.append(cmd)

    else:
        cmd = cmd[5:]
        string = f"{cmd}"
        if len(path) > 0:
            string = f"{'/'.join(path)}/{cmd}"
        prints.add(string)


for string in sorted(prints):
    print(f"git add {string}")

print('git commit')
print('git push')
