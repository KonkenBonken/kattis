jack, jill = (
    set(int(input()) for _ in range(int(x))) for x in input().split())

print(len(jack & jill))
