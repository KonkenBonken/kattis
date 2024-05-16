from math import floor, log10

L = int(input())


def encrypt(n):
    return n*floor(log10(n*10))


def steps():
    for p in range(1000, 0, -1):
        yield pow(10, p)


head = pow(10, 10)

for step in steps():
    encrypted = encrypt(head)
    is_less = encrypted < L
    multiply = is_less
    while True:
        next = head*step if multiply else head//step
        if next > 0 and is_less == (encrypt(next) < L):
            head = next
        else:
            break

for step in (100, 10, 3, 1):
    encrypted = encrypt(head)
    is_less = encrypted < L
    direction = 1 if is_less else -1
    while True:
        next = head+direction*step
        if next > 0 and is_less == (encrypt(next) < L):
            head = next
        else:
            break

print(head)
