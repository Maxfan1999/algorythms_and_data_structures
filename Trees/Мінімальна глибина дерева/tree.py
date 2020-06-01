class Node:
    def __init__(self, key=None):
        self.key = key
        self.left_child = None
        self.right_child = None

    def has_left(self):
        return self.left_child is not None

    def has_right(self):
        return self.right_child is not None

    def get_right(self):
        return self.right_child

    def get_left(self):
        return self.left_child

    def set_right(self, key):
        self.right_child = Node(key)

    def set_left(self, key):
        self.left_child = Node(key)


class BinarySearchTree(Node):
    def __init__(self):
        Node.__init__(self)
        self.size = 1000

    def put(self, item):
        node = self
        counter = 1
        while True:
            if node.key is None:
                node.key = item
                break
            elif item < node.key:
                if node.has_left():
                    node = node.left_child
                    continue
                else:
                    node.set_left(item)
                    break
                counter += 1
            elif item >= node.key:
                if node.has_right():
                    node = node.right_child
                    continue
                else:
                    node.set_right(item)
                    break
                counter += 1
            else:
                break
        if counter < self.size:
            self.size = counter


def dfs(tree):
    print(tree.key)
    if tree.has_left():
        dfs(tree.left_child)
    if tree.has_right():
        dfs(tree.right_child)


if __name__ == '__main__':
    input()
    seq = list(map(int, input().split()))
    tree = BinarySearchTree()
    for num in seq:
        tree.put(num)

#    dfs(tree)
    print(tree.size)


