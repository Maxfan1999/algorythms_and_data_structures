class PrefixTree:
    def __init__(self, key):
        self.key = key
        self.children = []

    def add_to_children(self, child):
        self.children.append(child)

    def get_child(self, key):
        for child in self.children:
            if child.key == key:
                return child

    def __contains__(self, item):
        return item in [child.key for child in self.children]


n = int(input())

for _ in range(n):
    k = int(input())
    flag = True
    main_tree = PrefixTree(0)
    current_node = main_tree
    phone_number = input()
    for ciphar in phone_number:
        current_node.add_to_children(PrefixTree(ciphar))
        current_node = current_node.get_child(ciphar)

    for i in range(k - 1):
        phone_number = input()
        index = 0
        in_tree = True
        current_node = main_tree
        while True:
            if phone_number[index] not in current_node:
                current_node.add_to_children(PrefixTree(phone_number[index]))
                if in_tree:
                    in_tree = False
            current_node = current_node.get_child(phone_number[index])
            if not current_node.children and in_tree:
                break
            index += 1
            if index == len(phone_number):
                break
        if in_tree:
            print("NO")
            flag = False
            break

    if flag:
        print("YES")




