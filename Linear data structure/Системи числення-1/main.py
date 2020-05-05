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
        return chr(ord("A") + n - 10)


binary_num = input()
dec_number = 0
n = len(binary_num)
for i in range(n):
    index = n - i - 1
    dec_number += 2 ** i * int(binary_num[index])

stack = StackOnList()

while dec_number > 0:
    stack.push(dec_number % 16)
    dec_number //= 16

number = ""
while not stack.is_empty():
    number = number + get_char_digit(stack.pop())
print(number)