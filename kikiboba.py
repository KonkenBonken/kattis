s = input()
k, b = s.count('k'), s.count('b')

if k == 0 and b == 0:
    print('none')
elif k < b:
    print('boba')
elif k > b:
    print('kiki')
else:
    print('boki')
