def reader():
    n, m = map(int, input().split())
    second_line = list(map(int, input().split()))
    database = DataBase(second_line)
    queries = [Query(*map(int, input().split())) for _ in range(m)]
    return n, m, database, queries


class Table:
    def __init__(self, index: int, size):
        self.index = index
        self.size = size
        self.parent = index

    def __str__(self):
        return f'Index: {self.index}, Size: {self.size}, Parent: {self.parent}'


class DataBase:
    def __init__(self, n):
        self.tables = [Table(i, n[i - 1]) for i in range(1, len(n) + 1)]
        self.max_size = max(n)

    def find(self, i):
        if i != self.tables[i-1].parent:
            self.tables[i-1].parent = self.find(self.tables[i-1].parent)
        return self.tables[i-1].parent

    def union(self, d_index, s_index):
        d_id = self.find(d_index)
        s_id = self.find(s_index)
        if d_id == s_id:
            return
        if self.tables[d_id - 1].size >= self.tables[s_id - 1].size:
            self.tables[s_id - 1].parent = d_id
            self.tables[d_id - 1].size += self.tables[s_id - 1].size
            if self.tables[d_id - 1].size > self.max_size:
                self.max_size = self.tables[d_id - 1].size
        else:
            self.tables[d_id - 1].parent = s_id
            self.tables[s_id - 1].size += self.tables[d_id - 1].size
            if self.tables[s_id - 1].size > self.max_size:
                self.max_size = self.tables[s_id - 1].size


class Query:
    def __init__(self, d_index, s_index):
        self.destination = d_index
        self.source = s_index

    def __str__(self):
        return f'Destination: {self.destination}, Source: {self.source}'


def run(database, queries):
    for query in queries:
        database.union(query.destination, query.source)
        print(database.max_size)


if __name__ == '__main__':
    n, m, database, queries = reader()
    run(database, queries)
