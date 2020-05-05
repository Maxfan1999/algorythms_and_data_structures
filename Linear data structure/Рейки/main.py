class StackOnList:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise Exception('Method "pop" is allowed only for not empty stack')
        res = self.items[-1]
        del self.items[-1]
        return res

    def top(self):
        if self.is_empty():
            raise Exception('Method "top" is allowed only for not empty stack')
        else:
            return self.items[-1]


def check(n, sequence):
    stack = StackOnList()
    for i in range(1, n + 1):
        stack.push(str(i))
        while not stack.is_empty() and stack.top() == sequence[0]:
            stack.pop()
            del sequence[0]
    if stack.is_empty():
        print("Yes")
    else:
        print("No")


while True:
    n = int(input())
    if n == 0:
        break
    else:
        while True:
            s = input()
            if s == "0":
                break
            else:
                sequence = s.split()
                check(n, sequence)
        print()
