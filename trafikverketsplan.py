N = int(input())
houses = tuple(set() for _ in range(N))

for _ in range(N-1):
    a, b = (int(x)-1 for x in input().split())
    houses[a].add(b)

for _ in range(int(input())):
    h, w = (int(x)-1 for x in input().split())

    queue = [h]
    for house in queue:
        if house == w:
            print('ja')
            break
        queue.extend(houses[house])
        houses[h].update(houses[house])
    else:
        print('nej')
