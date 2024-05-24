def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def solve(n, d, a, coords):
    cost = [-1] * n
    cost[0] = 0
    loop = True

    while loop:
        loop = False
        for i in range(n):
            for j in range(1, n):
                if i != j and cost[i] != -1:
                    new_cost = cost[i] + manhattan(coords[i], coords[j]) * d - a[j]

                    if cost[j] == -1 or new_cost < cost[j]:
                        cost[j] = new_cost
                        loop = True

    return str(cost[-1])


if __name__ == "__main__":
    n, d = map(int, input().split())
    a = [0] + list(map(int, input().split())) + [0]
    coords = []
    for _ in range(n):
        coords.append(tuple(map(int, input().split())))

    print(solve(n, d, a, coords))

# if __name__ == "__main__":
#     with open("input.txt", "r") as file:
#         n, d = map(int, file.readline().split())
#         a = [0] + list(map(int, file.readline().split())) + [0]
#         coords = []
#         for _ in range(n):
#             coords.append(tuple(map(int, file.readline().split())))
#
#     with open("output.txt", "w") as file:
#         file.write(solve(n, d, a, coords))



