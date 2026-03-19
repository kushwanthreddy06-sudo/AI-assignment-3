import heapq

def dijkstra(graph, start):
    # Initialize distances
    dist = {node: float('inf') for node in graph}
    dist[start] = 0

    pq = [(0, start)]  # (distance, node)

    while pq:
        current_dist, u = heapq.heappop(pq)

        # Skip if already processed
        if current_dist > dist[u]:
            continue

        for v, weight in graph[u]:
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                heapq.heappush(pq, (dist[v], v))

    return dist


# Example graph
graph = {
    'A': [('B', 4), ('C', 2)],
    'B': [('C', 5), ('D', 10)],
    'C': [('D', 3)],
    'D': []
}

print("Shortest distances:", dijkstra(graph, 'A'))