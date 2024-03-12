def reader():
    n = int(input())
    q = [input().split() for _ in range(n)]
    return q


class Command:
    def execute(self, number, name):
        raise NotImplementedError()


class Add(Command):
    def execute(self, number, name):
        book[number] = name


class Delete(Command):
    def execute(self, number, name):
        book.pop(number, None)


class Find(Command):
    def execute(self, number, name):
        return book.get(number, "not found")


instructions = {
    'add': Add(),
    'find': Find(),
    'del': Delete()
}

book = {

}

if __name__ == '__main__':
    queries = reader()
    for query in queries:
        query.append("")
        command = instructions[query[0]]
        output = command.execute(query[1], query[2])
        if output:
            print(output)
