while True:
    try:
        input()
        seq = list(enumerate(int(x) for x in input().split()))
        best = []

        def subseq(sub: 'list[int]', start: int):
            global best

            for i, n in seq[start + 1:]:
                if n > seq[sub[-1]][1]:
                    if len(sub) + len(seq) - i - 1 > len(best):
                        subseq(sub.copy(), i+1)
                    sub.append(i)

            if len(sub) > len(best):
                best = sub

        for s in range(len(seq)):
            if len(seq) - s > len(best):
                subseq([seq[s][0]], s)

        print(len(best))
        print(*best)

    except EOFError:
        break
