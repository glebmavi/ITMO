import sys


def solve(str_iter):
    output = []
    cases = int(next(str_iter))
    for _ in range(cases):
        next(str_iter)  # Skip the empty line
        n, m = map(int, next(str_iter).split())
        points = [[x, w, i] for i, (x, w) in enumerate(map(int, next(str_iter).split()) for _ in range(m))]

        reserved_points = sorted(points, key=lambda p: p[1])[:2 * n]
        reserved_points.sort(key=lambda p: p[0])

        total_weight = sum(reserved_points[i][1] + reserved_points[~i][1] for i in range(n))

        output.append(str(total_weight))
        output.extend(f"{reserved_points[i][2] + 1} {reserved_points[~i][2] + 1}" for i in range(n))
    print("\n".join(output))


if __name__ == "__main__":
    lines = sys.stdin.readlines()
    solve(iter(lines))
