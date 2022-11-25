N, K = (int(n) for n in input().split())
Games = [1 if c == 'V' else -1 for c in input()]

attempts = [Games]

for length in range(1, N):
    for i in range(N-length):
        attempts.append(Games[i:i+length] )

print(sum(max(attempts, key=sum)))
