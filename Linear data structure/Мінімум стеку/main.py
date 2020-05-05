class Node:
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None

    def set_next_node(self, node):
        self.next = node


class RecursionStack:
    def __init__(self):
        self.top_node = None
        self.min_node = None

    def is_empty(self):
        return self.top_node is None

    def push(self, item):
        node = Node(item)
        if not self.is_empty():
            node.set_next_node(self.top_node)
        self.top_node = node
        if self.min_node is None:
            self.min_node = Node(item)
        else:
            if self.min_node.item >= item:
                new_min_node = Node(item)
                new_min_node.prev = self.min_node
                self.min_node = new_min_node

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")

        top_node = self.top_node
        item = top_node.item
        self.top_node = top_node.next
        if item == self.min_node.item:
            min_node = self.min_node
            self.min_node = min_node.prev
            del min_node
        del top_node
        return item

    def get_top(self):
        return self.top_node.item

    def get_min(self):
        return self.min_node.item


a = RecursionStack()
n = int(input())
for _ in range(n):
    commands = input().split()
    if commands[0] == "1":
        a.push(int(commands[1]))
    elif commands[0] == "2":
        a.pop()
    else:
        print(a.get_min())
