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


def get_char_digit(n):
    if n < 10:
        return str(n)
    else:
        return f"[{n}]"


def convert(dec_number, n):
    stack = StackOnList()
    while dec_number > 0:
        stack.push(dec_number % n)
        dec_number //= n
    return stack


dec_number = int(input())
syst = int(input())

stack = convert(dec_number, syst)

number = ""
while not stack.is_empty():
    number = number + get_char_digit(stack.pop())
print(number)