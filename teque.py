class deque:
    def __init__(self):
        self.a = 1
        self.b = 0
        self.d = dict()

    def af(self, num: int):
        self.a -= 1
        self.d[self.a] = num

    def ab(self, num: int):
        self.b += 1
        self.d[self.b] = num

    def popf(self):
        v = self.d[self.a]
        del self.d[self.a]
        self.a += 1
        return v

    def popb(self):
        v = self.d[self.b]
        del self.d[self.b]
        self.b -= 1
        return v

    def __getitem__(self, i: int):
        return self.d[self.a + i]

    def __len__(self):
        return self.b - self.a + 1


left, right = deque(), deque()

for _ in range(int(input())):
    cmd, num = input().split()
    num = int(num)

    if cmd == 'push_back':
        right.ab(num)

    elif cmd == 'push_front':
        left.af(num)

    elif cmd == 'push_middle':
        if (len(left) != len(right)) and (len(left) != len(right) + 1):

            while len(left) < len(right):
                left.ab(right.popf())

            while len(left) > len(right) + 1:
                right.af(left.popb())

        right.af(num)

    elif cmd == 'get':
        if num < len(left):
            print(left[num])
        else:
            print(right[num - len(left)])
