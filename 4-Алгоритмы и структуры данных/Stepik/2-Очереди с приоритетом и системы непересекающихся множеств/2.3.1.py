class MinHeap:
    def __init__(self, l):
        self.array = l
        self.movements = []
        self.build_heap()

    def build_heap(self):
        for item in range(len(self.array) // 2 + 1, -1, -1):
            self.move_down(item)

    def add_element(self, element):
        self.array.append(element)
        self.move_up(len(self.array) - 1)

    def remove_element(self, index):
        self.array[index] = self.array[-1]
        self.array.pop()
        self.move_down(index)

    def get_parent_index(self, index):
        return (index - 1) // 2

    def move_up(self, index):
        if index == 0:
            return
        parent = (index - 1) // 2
        if self.array[parent] > self.array[index]:
            self.movements.append((parent, index))
            self.array[index], self.array[parent] = self.array[parent], self.array[index]
            self.move_up(parent)

    def move_down(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        min_index = index
        if left < len(self.array) and self.array[left] < self.array[min_index]:
            min_index = left
        if right < len(self.array) and self.array[right] < self.array[min_index]:
            min_index = right
        if index != min_index:
            self.movements.append((index, min_index))
            self.array[index], self.array[min_index] = self.array[min_index], self.array[index]
            self.move_down(min_index)

    def print_heap(self):
        print(*self.array, sep=' ')

    def print_movements(self):
        for move in self.movements:
            print(move[0], move[1])

    def print_movements_count(self):
        print(len(self.movements))


def draw_heap(array):
    def print_tree(index, level=0, prefix="Root: "):
        if index < len(array):
            print(" " * (level * 4) + prefix + "{" + str(array[index]) + "," + str(index) + "}")
            if 2 * index + 1 < len(array):
                print_tree(2 * index + 1, level + 1, "L-- ")
            if 2 * index + 2 < len(array):
                print_tree(2 * index + 2, level + 1, "R-- ")

    print_tree(0)


def reader():
    n = int(input())
    array = list(map(int, input().split()))
    return n, array



if __name__ == '__main__':
    n, array = reader()
    # draw_heap(array)
    heap = MinHeap(array)
    # draw_heap(heap.array)

    heap.print_movements_count()
    heap.print_movements()
    heap.print_heap()