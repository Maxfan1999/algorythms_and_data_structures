class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

    def set_next_node(self, node):
        self.next = node


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

first = RecursionQueue()
second = RecursionQueue()
n = int(input())
for i in map(int, input().split()):
    first.enqueue(i)

for i in map(int, input().split()):
    second.enqueue(i)

count = 0
is_draw = False
while (not first.is_empty()) and (not second.is_empty()):
    first_cart = first.dequeque()
    second_cart = second.dequeque()
    if first_cart == n - 1 and second_cart == 0:
        second.enqueue(first_cart)
        second.enqueue(second_cart)
    elif second_cart == n - 1 and first_cart == 0:
        first.enqueue(first_cart)
        first.enqueue(second_cart)
    elif second_cart > first_cart:
        second.enqueue(first_cart)
        second.enqueue(second_cart)
    else:
        first.enqueue(first_cart)
        first.enqueue(second_cart)
    count += 1
    if count > 2 * 10 ** 5:
        is_draw = True
        break
if is_draw:
    print("draw")
elif first.is_empty():
    print("second", count)
else:
    print("first", count)
