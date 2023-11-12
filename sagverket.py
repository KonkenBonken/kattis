# Group 1&2: N=1|2
N, T = (int(x) for x in input().split())

start_num = 10**9
print('?', start_num)

if T == 1:
    response = int(input())
    print('!', start_num - response)
elif T == 2:
    response = [int(x) for x in input().split()]
    x = start_num-response[0]
    print('?', x)
    print(response)
    response = [int(x) for x in input().split()]
    print(response)

    y = start_num-response[0]
    print('!', x, y)
