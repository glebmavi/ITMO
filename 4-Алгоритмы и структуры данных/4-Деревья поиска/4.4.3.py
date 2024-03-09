import sys

sys.setrecursionlimit(10 ** 5)

def reader(i: int):
    result = []
    for _ in range(i):
        values = list(map(int, input().split()))
        result.append(values)

    return result


class Tree:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return f"Value = {self.value}, left = ({self.left}), right = ({self.right})"

    def is_binary_search_tree(self, min_val=float('-inf'), max_val=float('inf')):
        if self.value < min_val or self.value >= max_val:
            return False

        if self.left != -1 and not self.left.is_binary_search_tree(min_val, self.value):
            return False
        if self.right != -1 and not self.right.is_binary_search_tree(self.value, max_val):
            return False

        return True


if __name__ == '__main__':
    nodes = reader(int(input()))
    tree_nodes = []
    for i in range(len(nodes)):
        tree_nodes.append(Tree(nodes[i][0], nodes[i][1], nodes[i][2]))

    for i in tree_nodes:
        if i.left != -1:
            i.left = tree_nodes[i.left]
        if i.right != -1:
            i.right = tree_nodes[i.right]

    print("CORRECT" if len(tree_nodes) == 0 or tree_nodes[0].is_binary_search_tree() else "INCORRECT")
