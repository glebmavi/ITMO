def solve(str):
    n, I = map(int, next(str).split())
    a = list(map(int, next(str).split()))
    a.sort()
    I *= 8
    k = int(pow(2, I // n))

    b = [0]
    for i in range(1, n):
        if a[i] != a[i - 1]:
            b.append(i)

    if len(b) <= k:
        print(0)
        return
    else:
        print(n - max(b[i + k] - b[i] for i in range(len(b) - k)))


if __name__ == "__main__":
    f = input()
    s = input()
    lines = [f, s]
    solve(iter(lines))
