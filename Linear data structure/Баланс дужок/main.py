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


def brackets_checker(s):
    stack_obj = StackOnList()
    for i in s:
        if i == '(' or i == "[":
            stack_obj.push(i)
        elif i == ")" or i == "]":
            if stack_obj.is_empty():
                return False
            else:
                if i == ')' and stack_obj.top() == '(' or i == ']' and stack_obj.top() == '[':
                    stack_obj.pop()

    if stack_obj.is_empty():
        return True
    else:
        return False


for _ in range(int(input())):
    flag = brackets_checker(input())
    if flag:
        print("Yes")
    else:
        print("No")
