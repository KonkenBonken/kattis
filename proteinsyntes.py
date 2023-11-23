from collections import deque

input()
T = input()
proteins = sorted((input()
                  for _ in range(int(input()))), key=len, reverse=True)

queue = deque((p, 1) for p in proteins)

while True:
    p, i = queue.popleft()
    if p == T:
        print(i)
        break
    queue.extend((p+q, i+1) for q in proteins)
