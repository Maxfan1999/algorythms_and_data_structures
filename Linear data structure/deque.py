class Node:
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None

    def set_next(self, node):
        self.next = node

    def set_prev(self, node):
        self.prev = node


class Deque:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue_left(self, item):
        self.items.insert(0, item)

    def enqueue_right(self, item):
        self.items.append(item)

    def dequeue_left(self):
        if self.is_empty():
            raise Exception("Deque is empty")
        return self.items.pop(0)

    def dequeue_right(self):
        if self.is_empty():
            raise Exception("Deque is empty")
        return self.items.pop()


class RecursionDeque:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None and self.tail is None

    def append_left(self, item):
        new_node = Node(item)
        new_node.next = self.head
        if self.is_empty():
            self.tail = new_node
        else:
            self.head.prev = new_node
        self.head = new_node

    def append(self, item):
        new_node = Node(item)
        new_node.prev = self.tail
        if self.is_empty():
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node

    def pop_left(self):
        if self.is_empty():
            raise Exception('Deque is empty')

        node = self.head
        item = node.item
        self.head = node.next
        del node
        return item

    def pop_right(self):
        if self.is_empty():
            raise Exception('Deque is empty')

        node = self.tail
        item = node.item
        self.tail = node.prev
        del node
        return item

    def get_all_items(self):
        node = self.head
        items = [node.item]
        while True:
            node = node.next
            items.append(node.item)
            if node == self.tail:
                break
        return items


if __name__ == "__main__":
    a = Deque()
    b = RecursionDeque()
    import random
    for i in range(20):
        num = random.randint(1, 100)
        a.enqueue_right(num)
        b.append(num)
    print(a.items)
    print(b.get_all_items())
    for i in range(10):
        flag = random.randint(0, 1)
        if flag:
            print("Left")
            a.dequeue_left()
            b.pop_left()
        else:
            print("Right")
            a.dequeue_right()
            b.pop_right()
        print(a.items)
        print(b.get_all_items())
