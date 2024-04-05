def solve(f):
    n = int(next(f))
    a = list(map(int, next(f).split()))
    b = list(map(int, next(f).split()))

    swaps = []

    for i in range(n):
        if a[i] != b[i]:
            for j in range(i + 1, n):
                if b[j] == a[i]:
                    for k in range(j, i, -1):
                        b[k], b[k-1] = b[k-1], b[k]
                        swaps.append((k-1, k))
                    break

    print(len(swaps))
    for i, j in swaps:
        print(i + 1, j + 1)

    return a, b


def test(goal, init):
    assert goal == init, f"Expected {goal} but got {init}"
    print("Passed")
    print("Expected:", goal)
    print("Got:", init)


if __name__ == "__main__":
    # input from console
    f = input()
    s = input()
    t = input()
    lines = [f, s, t]
    a, b = solve(iter(lines))
    test(a, b)
