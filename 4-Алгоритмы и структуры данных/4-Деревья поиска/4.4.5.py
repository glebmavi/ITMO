def reader():
    text = input()
    queries = [list(map(int, input().split())) for _ in range(int(input()))]
    return text, queries


def run():
    text, queries = reader()
    for l, r, k in queries:
        sub = text[l:r + 1]
        text = text[:l] + text[r + 1:]
        text = text[:k] + sub + text[k:]
    print(text)


if __name__ == '__main__':
    run()
