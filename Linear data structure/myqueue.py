import sys
sys.path.append(".")
from stack import Node


class Queue:
    def __init__(self):
        self.items = []

    def __len__(self):
        return len(self.items)

    def is_empty(self):
        return len(self) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        else:
            return self.items.pop(0)

    def show_head(self):
        return self.items[0]

    def show_tail(self):
        return self.items[-1]


class RecursionQueue:
    def __init__(self):
        self.front = None
        self.back = None

    def is_empty(self):
        return self.front is None and self.back is None

    def enqueue(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.front = new_node
        else:
            self.back.set_next_node(new_node)
        self.back = new_node

    def dequeque(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        else:
            front_node = self.front
            item = front_node.item
            self.front = front_node.next
            if self.front is None:
                self.back = None
        return item


if __name__ == "__main__":
    import random
    a = Queue()
    b = RecursionQueue()
    for _ in range(100):
        num = random.randint(1, 1000)
        a.enqueue(num)
        b.enqueue(num)
    for _ in range(20):
        print(a.dequeue(), b.dequeque())
