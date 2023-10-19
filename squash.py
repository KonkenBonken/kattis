N, K = (int(n) for n in input().split())
Games = [1 if c == 'V' else -1 for c in input()]


def check(a, b):
    return not (a[1] < b[0] or b[1] < a[0])


best = [sum(Games)]
indexes = [(0, N - 1)]

for length in range(1, N):
    for i in range(N-length):
        val = sum(Games[i:i + length])
        index = (i, i + length - 1)
        if len(best) < K:
            best.append(val)
            indexes.append(index)
        elif val > min(best):
            j = best.index(min(best))
            if not check(indexes[(j+1) % 3], index) and not check(indexes[(j+2) % 3], index):
                best[j] = val
                indexes[j] = index

        print(best)
        print(indexes)
print(best)
print(sum(best))
