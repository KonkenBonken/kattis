N = int(input())

if N < 99:
    print(99)
    exit()

N += 1
a = (N//100) * 100
b = a+100

if N-a >= b-N:
    print(b-1)
else:
    print(a-1)
