import heapq

def dijkstra(graph, start):
    
    dist = {node: float('inf') for node in graph}
    dist[start] = 0

    pq = [(0, start)]  

    while pq:
        current_dist, u = heapq.heappop(pq)

        
        if current_dist > dist[u]:
            continue

        for v, weight in graph[u]:
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                heapq.heappush(pq, (dist[v], v))

    return dist



graph = {
    'A': [('B', 4), ('C', 2)],
    'B': [('C', 5), ('D', 10)],
    'C': [('D', 3)],
    'D': []
}

print("Shortest distances:", dijkstra(graph, 'A'))
