def solve(f):
    n, k = map(int, next(f).split())
    a = list(map(int, next(f).split()))
    b = sorted(a)
    l, r = 0, n-1
    max_median = 0

    while l <= r:
        m = (l + r) // 2
        mn = 0
        prefix = [1 if i >= b[m] else -1 for i in a]
        for i in range(n):
            prefix[i] += prefix[i - 1] if i > 0 else 0
            if i >= k - 1:
                if prefix[i] - mn > 0:
                    l, max_median = m + 1, b[m]
                    break
                mn = min(mn, prefix[i - k + 1])
        else:
            r = m - 1

    print(max_median)


if __name__ == "__main__":
    # input from console
    f = input()
    s = input()
    lines = [f, s]
    solve(iter(lines))

    # input from file
    # with open("CMaxMedian.txt") as f:
    #     solve(f)
