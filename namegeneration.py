N = int(input())
names = set()

vw, vl = ('a', 'e', 'i', 'o', 'u'), 5
cn, cl = ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm',
          'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'), 21

long_length = N+21
long_gen = (
    cn[a % cl] + vw[b % vl] + cn[c % cl] + vw[d % vl] + cn[e % cl] + vw[f % vl]
    for f in range(vl)
    for e in range(vl)
    for d in range(vl)
    for c in range(cl)
    for b in range(cl)
    for a in range(cl)
)

long_name = ''.join(next(long_gen) for _ in range(long_length//6))

used_names = set()

for l in range(3, 21):
    i = 0
    while len(used_names) < N:
        name = long_name[i:i+l]
        i += 1
        if name in used_names:
            break
        print(name)
        used_names.add(name)
