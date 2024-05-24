def solve(grid, n, m):
    max_volume = 0
    seen = set()

    def dfs(i, j):
        stack = [(i, j)]
        volume = 0
        while stack:
            i, j = stack.pop()
            if (i, j) in seen:
                continue
            seen.add((i, j))
            volume += grid[i][j]
            for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= x < n and 0 <= y < m and grid[x][y] != 0:
                    stack.append((x, y))
        return volume

    for i in range(n):
        for j in range(m):
            if (i, j) not in seen and grid[i][j] != 0:
                max_volume = max(max_volume, dfs(i, j))

    return max_volume


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        grid = []
        for _ in range(n):
            grid.append(list(map(int, input().split())))
        print(solve(grid, n, m))
