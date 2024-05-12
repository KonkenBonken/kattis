# NOT SOLVED

K, N = (int(x) for x in input().split())

if (N == 1 or K == 2):
    print('YES')
elif (
    N % 2 == 1 or
    (N >= K and (N-K) % 2 == 0)
):
    print('MAYBE')
else:
    print('NO')
