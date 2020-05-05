class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

    def set_next_node(self, node):
        self.next = node


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def insert(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def get_head(self):
        return self.head.item

    def get_tail(self):
        if self.is_empty():
            raise Exception("List is empty")
        self.head = self.head.next
        return self.head


class ListWithCurrent:
    def __init__(self):
        self.first = None
        self.prev = None
        self.curr = None

    def is_empty(self):
        return self.first is None

    def insert(self, item):
        node = Node(item)
        node.next = self.curr
        if self.curr == self.first:
            self.first = node
        if self.prev is not None:
            self.prev.next = node
        self.prev = node

    def next(self):
        if self.is_empty():
            raise Exception("Error in 'next': ListWithCurrent is empty")
        elif self.curr.next is None:
            raise StopIteration
        else:
            self.prev = self.curr
            self.curr = self.curr.next

    def set_first_as_current(self):
        if self.is_empty():
            raise Exception("Error in 'set_first_as_curr': ListWithCurrent is empty")
        else:
            self.curr = self.first
            self.prev = None

    def get_curr(self):
        if self.is_empty():
            raise Exception("Error in 'get_curr': ListWithCurrent is empty")
        else:
            return self.curr

    def __iter__(self):
        return ListIterator(self)


class NodeWithTwoLinks:
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.curr = None

    def is_empty(self):
        return self.first is None

    def set_first_as_current(self):
        if self.is_empty():
            raise Exception("Error in 'set_first_as_current': DoubleLinkedList is empty")
        self.curr = self.first

    def set_last_as_current(self):
        if self.is_empty():
            raise Exception("Error in 'set_last_as_current': DoubleLinkedList is empty")
        self.curr = self.last

    def next(self):
        if self.is_empty():
            raise Exception("Error in 'next': DoubleLinkedList is empty")
        self.curr = self.curr.next

    def prev(self):
        if self.is_empty():
            raise Exception("Error in 'prev': DoubleLinkedList is empty")
        self.curr = self.curr.prev

    def get_current(self):
        if self.is_empty():
            raise Exception("Error in 'get_current': DoubleLinkedList is empty")
        return self.curr.item

    def insert_before_current(self, item):
        node = NodeWithTwoLinks(item)
        node.next = self.curr
        if self.is_empty():
            self.last = self.first = self.curr = node
        else:
            if self.curr == self.first:
                self.first = node
            else:
                node.prev = self.curr.prev
                self.curr.prev.next = node
        self.curr.prev = node

    def insert_after_current(self, item):
        node = NodeWithTwoLinks(item)
        node.prev = self.curr
        if self.is_empty():
            self.last = self.first = self.curr = node
        else:
            if self.curr == self.last:
                self.last = node
            else:
                node.next = self.curr.next
                self.curr.next.prev = node
        self.curr.next = node
        self.curr = node

    def delete_current(self):
        if self.is_empty():
            raise Exception("Error in 'delete_current': DoubleLinkedList is empty")
        current_node = self.curr
        if current_node == self.first:
            new_first_node = self.first.next
            new_first_node.prev = None
            self.first = new_first_node
        elif current_node == self.last:
            new_last_node = self.last.prev
            new_last_node.next = None
            self.last = new_last_node
        else:
            current_node.prev.next = current_node.next
            current_node.next.prev = current_node.prev
        del current_node

    def __iter__(self):
        return ListIterator(self)


class ListIterator:
    def __init__(self, lst):
        self.cursor = lst.first

    def __next__(self):
        if self.cursor is None:
            raise StopIteration
        else:
            item = self.cursor.item
            self.cursor = self.cursor.next
            return item


if __name__ == "__main__":
    import random
    a = DoubleLinkedList()
    for _ in range(10):
        num = random.randint(1, 100)
        print(num, end=" ")
        a.insert_before_current(num)
    print()
    a.set_first_as_current()
    while a.curr is not None:
        print(a.curr.item, end=" ")
        a.next()
    a.set_first_as_current()
    for i in a:
        print(i, end=" ")
    print()
