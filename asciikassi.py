N = int(input())

print('+' + ''.join('-' for _ in range(N)) + '+')

for _ in range(N):
    print('|' + ''.join(' ' for _ in range(N)) + '|')


print('+' + ''.join('-' for _ in range(N)) + '+')
