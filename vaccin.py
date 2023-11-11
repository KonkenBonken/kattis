input()
days = [int(x) for x in input().split()]
people = [int(x) for x in input().split()]

for j, queue in enumerate(people):
    queue += 1
    for i, vaccins in enumerate(days):
        queue -= vaccins
        if queue <= 0:
            print(i+1)
            break
    else:
        print(-1)
