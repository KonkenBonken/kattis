from collections import deque
from sys import setrecursionlimit
setrecursionlimit(10**6)

input()
T = input()
proteins = [input() for _ in range(int(input()))]


queue = deque((p, 1) for p in proteins)

while True:
    p, i = queue.popleft()
    if p == T:
        print(i)
        break
    queue.extend((p+q, i+1) for q in proteins)
