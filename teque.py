from collections import deque


teque = deque()

for _ in range(int(input())):
    cmd, num = input().split()
    num = int(num)

    if cmd == 'push_back':
        teque.append(num)
    elif cmd == 'push_front':
        teque.appendleft(num)
    elif cmd == 'push_middle':
        teque.insert((len(teque)+1)//2, num)
    elif cmd == 'get':
        print(teque[num])
