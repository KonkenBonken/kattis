N = int(input())
names = set()

v = ('a', 'e', 'i', 'o', 'u')
c = ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm',
     'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z')

i = 0
while len(names) < N:
    name = c[i % 21] + v[(i+1) % 5] + c[(i+2) % 21]
    i += 1
    if name not in names:
        names.add(name)
        print(name)
