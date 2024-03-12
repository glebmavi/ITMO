# Tests passed with python 3 not 3.10

import sys


class Node:
    def __init__(self, value, left, right, parent):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent
        self.sum = value

    def __str__(self):
        return f"Node(Value={self.value}, Sum={self.sum})"


class SplayTree:
    def __init__(self, root):
        self.root = root
        self.s = 0
        self.min = None
        self.max = None

    def left_rotate(self, node):
        y = node.right
        if y is not None:
            node.right = y.left
            if y.left is not None:
                y.left.parent = node
            y.parent = node.parent
            y.left = node
        if node.parent is None:
            self.root = y
        elif node == node.parent.left:
            node.parent.left = y
        else:
            node.parent.right = y
        node.parent = y
        self.update_sum(node)
        self.update_sum(y)

    def right_rotate(self, node):
        y = node.left
        if y is not None:
            node.left = y.right
            if y.right is not None:
                y.right.parent = node
            y.parent = node.parent
            y.right = node
        if node.parent is None:
            self.root = y
        elif node == node.parent.left:
            node.parent.left = y
        else:
            node.parent.right = y
        node.parent = y
        self.update_sum(node)
        self.update_sum(y)

    def splay(self, node):
        while node.parent is not None:
            if node.parent.parent is None:
                if node == node.parent.left:
                    self.right_rotate(node.parent)
                else:
                    self.left_rotate(node.parent)
            elif node == node.parent.left and node.parent == node.parent.parent.left:
                self.right_rotate(node.parent.parent)
                self.right_rotate(node.parent)
            elif node == node.parent.right and node.parent == node.parent.parent.right:
                self.left_rotate(node.parent.parent)
                self.left_rotate(node.parent)
            elif node == node.parent.right and node.parent == node.parent.parent.left:
                self.left_rotate(node.parent)
                self.right_rotate(node.parent)
            else:
                self.right_rotate(node.parent)
                self.left_rotate(node.parent)

    def insert(self, node: Node):
        if self.root is None:
            self.root = node
            self.min = node
            self.max = node
            return
        current = self.root
        while True:
            if node.value == current.value:
                self.splay(current)
                return
            elif node.value < current.value:
                if current.left is None:
                    current.left = node
                    node.parent = current
                    self.splay(node)
                    if node.value < self.min.value:
                        self.min = node
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = node
                    node.parent = current
                    self.splay(node)
                    if node.value > self.max.value:
                        self.max = node
                    return
                current = current.right

    def find(self, value):
        if self.root is None or value < self.min.value or value > self.max.value:
            return None
        current = self.root
        while current is not None:
            if value == current.value:
                self.splay(current)
                return current
            elif value < current.value:
                if current.left is None:
                    return None
                current = current.left
            else:
                if current.right is None:
                    return None
                current = current.right
        return None

    def find_min(self, node):  # searches only in subtree
        if node is None:
            return None
        while node.left is not None:
            node = node.left
        return node

    def find_max(self, node):  # searches only in subtree
        if node is None:
            return None
        while node.right is not None:
            node = node.right
        return node

    def remove(self, value):
        node = self.find(value)
        if node is None:
            return
        if node.left:
            local_max = self.find_max(node.left)
            self.splay(local_max)
            local_max.right = node.right
            if node.right:
                node.right.parent = local_max
            self.root = local_max
            self.root.parent = None
            self.max = self.find_max(self.root)
        else:
            self.root = node.right
            if self.root is not None:
                self.root.parent = None
            self.min = self.find_min(self.root)
        self.update_sum(self.root)

    def update_sum(self, node):
        if node:
            node.sum = node.value + (node.left.sum if node.left else 0) + (node.right.sum if node.right else 0)

    def f(self, x):
        return (x + self.s) % 1000000001

    def find_min_in_range(self, node, min_limit):
        current = node
        result = None
        while current is not None:
            if current.value >= min_limit:
                result = current
                current = current.left
            else:
                current = current.right
        return result

    def find_max_in_range(self, node, max_limit):
        current = node
        result = None
        while current is not None:
            if current.value <= max_limit:
                result = current
                current = current.right
            else:
                current = current.left
        return result

    def sum(self, left, right):
        if left > right or self.root is None or left > self.max.value or right < self.min.value:
            self.s = 0
            return self.s
        if left == right:
            node = self.find(left)
            if node:
                self.s = node.value
            else:
                self.s = 0
            return self.s
        self.s = self.root.sum
        leftest = self.find_min_in_range(self.root, left)
        if leftest is not None:
            self.splay(leftest)
            if leftest.left is not None:
                self.s -= leftest.left.sum
        rightest = self.find_max_in_range(self.root, right)
        if rightest is not None:
            self.splay(rightest)
            if rightest.right is not None:
                self.s -= rightest.right.sum
        return self.s


# def run():
#     tree = SplayTree(None)
#     commands = sys.stdin.read().split('\n')[1:-1]  # Skip the first line and the last empty line
#     commands = [command.split() for command in commands]
#     for i in commands:
#         value = tree.f(int(i[1]))
#         if i[0] == "+":
#             tree.insert(Node(value, None, None, None))
#         elif i[0] == "?":
#             result = "Found\n" if tree.find(value) is not None else "Not found\n"
#             sys.stdout.write(result)
#             sys.stdout.flush()
#         elif i[0] == "-":
#             tree.remove(value)
#         elif i[0] == "s":
#             result = str(tree.sum(value, tree.f(int(i[2])))) + "\n"
#             sys.stdout.write(result)
#             sys.stdout.flush()


def run(filename):
    tree = SplayTree(None)
    with open(filename, 'r') as f:
        lines = f.readlines()
    for line in lines[1:]:  # Skip the first line
        i = line.split()
        value = tree.f(int(i[1]))
        if i[0] == "+":
            tree.insert(Node(value, None, None, None))
        elif i[0] == "?":
            result = "Found\n" if tree.find(value) is not None else "Not found\n"
            sys.stdout.write(result)
            sys.stdout.flush()
        elif i[0] == "-":
            tree.remove(value)
        elif i[0] == "s":
            result = str(tree.sum(value, tree.f(int(i[2])))) + "\n"
            sys.stdout.write(result)
            sys.stdout.flush()


if __name__ == '__main__':
    run("a.txt")
    # run()

