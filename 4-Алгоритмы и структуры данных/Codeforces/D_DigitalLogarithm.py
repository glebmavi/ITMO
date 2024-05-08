import heapq


def add_to_max_heap(max_heap, value):
    heapq.heappush(max_heap, -1 * value)


def pop_from_max_heap(max_heap):
    return -1 * heapq.heappop(max_heap)


def peek_max_heap(max_heap):
    return -1 * max_heap[0]


def digital_logarithm(x):
    return len(str(x))


def solve(n, a, b):
    steps = 0
    heap_a = []
    heap_b = []
    for i in range(n):
        add_to_max_heap(heap_a, a[i])
        add_to_max_heap(heap_b, b[i])

    while len(heap_a) > 0 and len(heap_b) > 0:
        steps += step(heap_a, heap_b)

    print(steps)


def step(heap_a, heap_b):
    peek_a = peek_max_heap(heap_a)
    peek_b = peek_max_heap(heap_b)

    if peek_a == peek_b:
        pop_from_max_heap(heap_a)
        pop_from_max_heap(heap_b)
        return 0
    else:
        if peek_a > peek_b:
            new = digital_logarithm(pop_from_max_heap(heap_a))
            add_to_max_heap(heap_a, new)
        else:
            new = digital_logarithm(pop_from_max_heap(heap_b))
            add_to_max_heap(heap_b, new)
        return 1


if __name__ == "__main__":
    tests = int(input())
    for i in range(tests):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        solve(n, a, b)
