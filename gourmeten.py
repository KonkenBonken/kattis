M = int(input())
courses = tuple(int(input())for _ in range(int(input())))
result = 0


def nxt(time, count):
    for course in courses:
        if course + time == M:
            global result
            result += 1
    for course in courses:
        if time + course < M:
            nxt(time + course, count+1)


nxt(0, 0)
print(result)
