class Heap:
    def __init__(self):
        self.items = [0]
        self.size = 0

    def is_empty(self):
        return len(self.items) == 1

    def insert(self, item):
        self.items.append(item)
        self.size += 1
        self.sit_up()

    def insert_min(self):
        root = self.items[1]
        self.items[1] = self.items[-1]
        self.items.pop()
        self.size -= 1
        self.sit_down()
        return root

    def sit_down(self):
        index = 1
        while 2 * index <= self.size:
            min_child = self.get_min_child(2 * index, 2 * index + 1)
            if self.items[min_child] < self.items[index]:
                self.swap(index, min_child)
            index = min_child

    def sit_up(self):
        index = len(self.items) - 1
        while index > 1:
            parent = index // 2
            if self.items[parent] > self.items[index]:
                self.swap(index, parent)
            index = parent

    def get_min_child(self, left_child, right_child):
        if right_child > self.size:
            return left_child
        if self.items[left_child] > self.items[right_child]:
            return right_child
        else:
            return left_child

    def swap(self, i, j):
        self.items[i], self.items[j] = self.items[j], self.items[i]


"""class PriorityQueue(Heap):
    def __init__(self):
        super().__init__()
        self.elements_map = {}

    def insert(self, item, prior):
        self.size += 1
        self.items.append(item)
        self.elements_map[item] = prior
        self.sit_up()

    def swap(self, i, j):
        pos_i = self.items[i]
        pos_j = self.items[j]
        k = self.elements_map[pos_i]
        self.elements_map[pos_i] = self.elements_map[pos_j]
        self.elements_map[pos_j] = k
        super().swap(i, j)

    def insert_min(self):
        min_el = self.items[1]
        self.items[1] = self.items[-1]
        pos = self.items[-1]"""


heap = Heap()
input()
for i in map(int, input().split()):
    heap.insert(i)

s = 0
while True:
    first_min = heap.insert_min()
    second_min = heap.insert_min()
    cost = first_min + second_min
    s += cost
    if heap.is_empty():
        break
    else:
        heap.insert(cost)
print(s)