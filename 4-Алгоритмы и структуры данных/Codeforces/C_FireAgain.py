def solve(n, m, k, trees):
    burning_trees = []
    for a in range(0, k * 2, 2):
        burning_trees.append((trees[a], trees[a + 1]))
    last_cost = None
    last_tree = (-1, -1)

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            cost = min([abs(i - t[0]) + abs(j - t[1]) for t in burning_trees])
            if last_cost is None or cost > last_cost:
                last_cost = cost
                last_tree = (i, j)

    return f"{last_tree[0]} {last_tree[1]}"


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        n, m = map(int, file.readline().split())
        k = int(file.readline())
        trees = list(map(int, file.readline().split()))

    with open("output.txt", "w") as file:
        file.write(solve(n, m, k, trees))
