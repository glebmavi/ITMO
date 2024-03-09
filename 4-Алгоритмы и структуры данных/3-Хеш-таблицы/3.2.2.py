from collections import deque


def reader():
    m = int(input())
    n = int(input())
    q = [input().split() for _ in range(n)]
    return m, n, q


def hash_string(string, m):
    h = 0
    x = 263
    p = 1000000007
    for i in range(len(string)):
        h += ord(string[i]) * (x ** i)
    return h % p % m


class Table:
    def __init__(self, m):
        self.m = m
        self.table = {i: deque() for i in range(m)}

    def add(self, data):
        hash = hash_string(data, self.m)
        if data not in self.table[hash]:
            self.table[hash].appendleft(data)

    def delete(self, data):
        hash = hash_string(data, self.m)
        if data in self.table[hash]:
            self.table[hash].remove(data)

    def find(self, data):
        hash = hash_string(data, self.m)
        return "yes" if data in self.table[hash] else "no"

    def check(self, data):
        return " ".join(self.table[int(data)])


def run():
    m, n, queries = reader()
    table = Table(m)

    for query in queries:
        output = None
        if query[0] == 'del':
            table.delete(query[1])
        else:
            output = getattr(table, query[0])(query[1])
        if output:
            print(output)


if __name__ == '__main__':
    run()
