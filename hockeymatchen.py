teamOne = [int(x) for x in input().split()]
teamTwo = [int(x) for x in input().split()]


def save(A, B):
    if A[0] == -1 and B[1] != -1 and B[2] != -1:
        A[0] = B[2]-B[1]
    if B[0] != -1 and A[1] == -1 and A[2] != -1:
        A[1] = A[2]-B[0]
    if B[0] != -1 and A[1] != -1 and A[2] == -1:
        A[2] = B[0]+A[1]


save(teamOne, teamTwo)
save(teamTwo, teamOne)

print(*teamOne)
print(*teamTwo)
