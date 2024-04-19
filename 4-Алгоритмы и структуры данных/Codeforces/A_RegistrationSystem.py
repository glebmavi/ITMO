def solve(lines):
    d = {}
    for l in lines:
        if l in d:
            d[l] += 1
            print(l + str(d[l]))
        else:
            d[l] = 0
            print("OK")


if __name__ == "__main__":
    n = int(input())
    lines = []
    for i in range(n):
        s = input()
        lines.append(s)
    solve(lines)
