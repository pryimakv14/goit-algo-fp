import heapq


def dijkstra(graph, start):
    dist_map = {vertex: float("infinity") for vertex in graph}
    dist_map[start] = 0
    heap = [(0, start)]

    while heap:
        current_distance, current_vertex = heapq.heappop(heap)

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < dist_map[neighbor]:
                dist_map[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))

    return dist_map


if __name__ == "__main__":
    graph = {
        "A": {"B": 2, "C": 4, "D": 7},
        "B": {"A": 2, "C": 1, "E": 3},
        "C": {"A": 4, "B": 1, "D": 2, "E": 1},
        "D": {"A": 7, "C": 2, "E": 5},
        "E": {"B": 3, "C": 1, "D": 5}
    }
    print(f"Shortest distances from A: ", dijkstra(graph, "A"))
