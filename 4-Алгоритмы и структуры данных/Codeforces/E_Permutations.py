import itertools


def permutations(data, k):
    answer = 100000000
    for i in itertools.permutations(range(k)):
        mn, mx = 100000000, -100000000
        for j in data:
            num = ''
            for l in i:
                num += j[l]
            num = int(num)
            mx = max(mx, num)
            mn = min(mn, num)
        m = mx - mn
        answer = min(answer, m)

    return answer


if __name__ == "__main__":
    n, k = map(int, input().split())
    data = []
    for i in range(n):
        data.append(input())
    print(permutations(data, k))
