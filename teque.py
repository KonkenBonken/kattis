from collections import deque


left, right = deque(), deque()

for _ in range(int(input())):
    cmd, num = input().split()
    num = int(num)

    if cmd == 'push_back':
        right.append(num)

    elif cmd == 'push_front':
        left.appendleft(num)

    elif cmd == 'push_middle':
        if (len(left) != len(right)) and (len(left) != len(right) + 1):

            while len(left) < len(right):
                left.append(right.popleft())

            while len(left) > len(right) + 1:
                right.appendleft(left.pop())

        right.appendleft(num)

    elif cmd == 'get':
        if num < len(left):
            print(left[num])
        else:
            print(right[num - len(left)])
