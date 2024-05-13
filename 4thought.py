ops = {'*', '+', '-', '//'}


def case(N):
    for a in ops:
        for b in ops:
            for c in ops:
                if int(eval(f'4{a}4{b}4{c}4')) == N:
                    print(f'4 {a} 4 {b} 4 {c} 4 = {N}'.replace('//', '/'))
                    return
    print('no solution')


for _ in range(int(input())):
    case(int(input()))
