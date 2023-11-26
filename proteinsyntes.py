from collections import deque

input()
T = input()
proteins = sorted((p for p in (input()
                  for _ in range(int(input()))) if p in T), key=len, reverse=True)

L, M = len(T), min(len(p) for p in proteins)
queue = deque([(1, proteins)])

while len(queue) > 0:
    i, subqueue = queue.popleft()
    for p in subqueue:
        if p == T:
            print(i)
            break
        if len(p) <= L-M:
            queue.append(
                (i+1, [p+q for q in proteins if p+q in T and len(p+q) <= L]))
    else:
        continue
    break
