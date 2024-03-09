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

    def in_order(self):
        result = []
        if self.left != -1:
            result.extend(self.left.in_order())
        result.append(self.value)
        if self.right != -1:
            result.extend(self.right.in_order())
        return result

    def pre_order(self):
        result = [self.value]
        if self.left != -1:
            result.extend(self.left.pre_order())
        if self.right != -1:
            result.extend(self.right.pre_order())
        return result

    def post_order(self):
        result = []
        if self.left != -1:
            result.extend(self.left.post_order())
        if self.right != -1:
            result.extend(self.right.post_order())
        result.append(self.value)
        return result


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

    print(*tree_nodes[0].in_order())
    print(*tree_nodes[0].pre_order())
    print(*tree_nodes[0].post_order())


