class Tree:
    def __init__(self, value, parent=None):
        self.value = value
        self.parent = parent
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def print_tree(self):

        print(self.value, self.children)
        for child in self.children:
            child.print_tree()

    def print_height(self):
        height = 1
        if not self.children:
            return height

        queue = [(self, height)]
        while queue:
            node, height = queue.pop(0)
            if node.children:
                for child in node.children:
                    queue.append((child, height + 1))

        return height


def reader(n: int, row: str):
    list = row.split()
    nodes = [Tree(i) for i in range(n)]
    root = None
    for i, node in enumerate(nodes):
        if list[i] == '-1':
            root = node
        else:
            nodes[int(list[i])].add_child(node)

    return nodes, root


if __name__ == '__main__':
    # n = int(input())
    # row = input()
    n = 10
    row = "9 7 5 5 2 9 9 9 2 -1"
    nodes, root = reader(n, row)
    root.print_tree()
    print(root.print_height())
