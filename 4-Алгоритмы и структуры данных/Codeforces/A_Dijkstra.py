import heapq


def dijkstra(start, end):
    distances = [float('inf')] * (n + 1)
    distances[start] = 0
    previous_vertices = [-1] * (n + 1)
    heap = [(0, start)]

    while heap:
        current_distance, current_vertex = heapq.heappop(heap)
        if current_distance > distances[current_vertex]:
            continue
        for neighbour, weight in graph[current_vertex]:
            alternative_route = distances[current_vertex] + weight
            if alternative_route < distances[neighbour]:
                distances[neighbour] = alternative_route
                previous_vertices[neighbour] = current_vertex
                heapq.heappush(heap, (alternative_route, neighbour))

    if distances[end] == float('inf'):
        return [-1]
    else:
        path, current_vertex = [], end
        while current_vertex != -1:
            path.append(current_vertex)
            current_vertex = previous_vertices[current_vertex]
        path.reverse()
        return path


if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, weight = map(int, input().split())
        graph[a].append((b, weight))
        graph[b].append((a, weight))

    print(*dijkstra(1, n))
