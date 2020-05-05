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


class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

    def set_next_node(self, node):
        self.next = node


class RecursionStack:
    def __init__(self):
        self.top_node = None

    def is_empty(self):
        return self.top_node is None

    def push(self, item):
        node = Node(item)
        if not self.is_empty():
            node.set_next_node(self.top_node)
        self.top_node = node

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")

        top_node = self.top_node
        item = top_node.item
        self.top_node = top_node.next
        del top_node
        return item

    def get_top(self):
        return self.top_node.item


if __name__ == "__main__":
    import random
    a = StackOnList()
    b = RecursionStack()
    for _ in range(100):
        num = random.randint(1, 1000)
        a.push(num)
        b.push(num)
    for _ in range(20):
        print(a.pop(), b.pop())