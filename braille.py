BrailleDict = (
    '.***..', '*.....', '*.*...', '**....', '**.*..',
    '*..*..', '***...', '****..', '*.**..', '.**...'
)

Numbers = [0, 0]

for I in range(2):

    N = int(input())
    rows = [input().split() for _ in range(3)]
    numsStr = ['']*N

    for i in range(N):
        numsStr[i] = ''.join(map(lambda row: row[i], rows))

    Numbers[I] = int(''.join(
        map(lambda numStr: str(BrailleDict.index(numStr)), numsStr)
    ))


Brailles = tuple(BrailleDict[int(digit)] for digit in str(sum(Numbers)))
rows = ['']*3
for Braille in Brailles:
    rows[0] += Braille[0:2] + ' '
    rows[1] += Braille[2:4] + ' '
    rows[2] += Braille[4:6] + ' '

print('\n'.join(rows))
