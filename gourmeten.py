from math import factorial

M = int(input())
courses = tuple(int(input())for _ in range(int(input())))
repeated = tuple((course, courses.count(course))
                 for course in set(courses) if courses.count(course) > 1)
combinations = []
result = 0


def nxt(history):
    for course in set(courses):
        if course <= history[-1]:
            tpl = (*history, course)
            if sum(history) + course == M:
                combinations.append(tpl)
            elif sum(history) + course < M:
                nxt(tpl)


for course in set(courses):
    nxt((course,))
    if course == M:
        combinations.append((course,))

for history in combinations:
    current = factorial(len(history))
    for duplicate in set(history):
        current //= factorial(history.count(duplicate))
    for course, count in repeated:
        current *= count ** history.count(course)
    result += current

print(result)
