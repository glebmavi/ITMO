class Processor:
    def __init__(self, index):
        self.index = index
        self.time = 0

    def __lt__(self, other):
        if self.time == other.time:
            return self.index < other.index
        return self.time < other.time

    def __le__(self, other):
        if self.time == other.time:
            return self.index <= other.index
        return self.time <= other.time

    def __gt__(self, other):
        if self.time == other.time:
            return self.index > other.index
        return self.time > other.time

    def __ge__(self, other):
        if self.time == other.time:
            return self.index >= other.index
        return self.time >= other.time

    def __eq__(self, other):
        return self.time == other.time and self.index == other.index

    def __ne__(self, other):
        return self.time != other.time or self.index != other.index

    def __str__(self):
        return f'Index: {self.index}, Time: {self.time}'


# len in this case == amount of processors and will not change
class MinHeap:
    def __init__(self, l, m):
        self.array = l
        self.size = m

    def heapify(self):
        for item in range(self.size // 2 + 1, -1, -1):
            self.move_down(item)

    def add_element(self, element):
        self.array.append(element)
        self.move_up(self.size - 1)

    def remove_element(self, index):
        self.array[index] = self.array[-1]
        self.array.pop()
        self.move_down(index)

    def move_up(self, index):
        if index == 0:
            return
        parent = (index - 1) // 2
        if self.array[parent] > self.array[index]:
            self.array[index], self.array[parent] = self.array[parent], self.array[index]
            self.move_up(parent)

    def move_down(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        min_index = index
        if left < self.size and self.array[left] < self.array[min_index]:
            min_index = left
        if right < self.size and self.array[right] < self.array[min_index]:
            min_index = right
        if index != min_index:
            self.array[index], self.array[min_index] = self.array[min_index], self.array[index]
            self.move_down(min_index)

    def print_heap(self):
        print(*self.array, sep=' ')


def reader():
    first_line = list(map(int, input().split()))
    second_line = list(map(int, input().split()))
    n = first_line[0]
    m = first_line[1]
    return n, m, second_line


def run():
    processors, n, second_line = reader()
    result = []
    temp = []
    for processor in range(processors):
        temp.append(Processor(processor))
    processors_queue = MinHeap(temp, processors)

    while second_line:
        result.append([processors_queue.array[0].index, processors_queue.array[0].time])
        processors_queue.array[0].time += second_line.pop(0)
        processors_queue.move_down(0)

    return result


if __name__ == '__main__':
    for i in run():
        print(*i)
