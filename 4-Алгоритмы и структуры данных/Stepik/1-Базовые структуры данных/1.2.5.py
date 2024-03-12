from collections import deque


def reader():
    n = int(input())
    array = list(map(int, input().split()))
    m = int(input())
    return n, array, m


def max_in_sliding_window(nums, m):
    if not nums:
        return []
    window = deque()
    result = []
    for i, num in enumerate(nums):
        while window and window[0] < i - m + 1:
            window.popleft()
        while window and nums[window[-1]] < num:
            window.pop()
        window.append(i)
        if i >= m - 1:
            result.append(nums[window[0]])

    return result


if __name__ == '__main__':
    n, array, m = reader()
    print(*max_in_sliding_window(array, m), sep=' ')
