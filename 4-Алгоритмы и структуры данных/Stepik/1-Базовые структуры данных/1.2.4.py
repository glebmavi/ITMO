def reader():
    operations = []
    n = int(input())
    for i in range(n):
        operations.append(input())

    return operations


class max_stack:
    def __init__(self):
        self.stack = []
        self.max = []

    def push(self, value):
        self.stack.append(value)
        if len(self.max) == 0 or value >= self.max[-1]:
            self.max.append(value)

    def pop(self):
        if self.stack[-1] == self.max[-1]:
            self.max.pop()
        self.stack.pop()

    def get_max(self):
        if len(self.max) == 0:
            return 0
        return self.max[-1]


def run():
    operations = reader()
    stack = max_stack()
    for operation in operations:
        if operation.startswith('push'):
            stack.push(int(operation.split()[1]))
        elif operation == 'pop':
            stack.pop()
        elif operation == 'max':
            print(stack.get_max())
        else:
            print("Unknown operation")


if __name__ == '__main__':
    run()
