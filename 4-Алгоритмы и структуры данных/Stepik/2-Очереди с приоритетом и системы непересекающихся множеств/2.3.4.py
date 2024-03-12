def reader():
    n, e, d = map(int, input().split())
    eq = [Query(*map(int, input().split())) for _ in range(e)]
    dq = [Query(*map(int, input().split())) for _ in range(d)]
    return n, e, d, eq, dq


class Query:
    def __init__(self, d_index, s_index):
        self.destination = d_index
        self.source = s_index

    def __str__(self):
        return f'Destination: {self.destination}, Source: {self.source}'


class Variable:
    def __init__(self, name):
        self.name = name
        self.parent = name

    def __str__(self):
        return f'Name: {self.name}, Parent: {self.parent}'


class DisJoinSet:
    def __init__(self, n):
        self.set = [Variable(i) for i in range(1, n + 1)]

    def find(self, i):
        if i != self.set[i - 1].parent:
            self.set[i - 1].parent = self.find(self.set[i - 1].parent)
        return self.set[i - 1].parent

    def union(self, d_index, s_index):
        d_id = self.find(d_index)
        s_id = self.find(s_index)
        if d_id == s_id:
            return
        self.set[s_id - 1].parent = self.set[d_id - 1].parent


def run(n, e, d, equal_queries, different_queries):
    system = DisJoinSet(n)
    for query in equal_queries:
        system.union(query.destination, query.source)
    for query in different_queries:
        if system.find(query.destination) == system.find(query.source):
            return 0
    return 1


if __name__ == '__main__':
    n, e, d, eq, dq = reader()
    print(n, e, d, sep=' ')
    for item in eq:
        print(item)
    for item in dq:
        print(dq)

    system = DisJoinSet(n)
    print(*system.set)

    print(run(n, e, d, eq, dq))
