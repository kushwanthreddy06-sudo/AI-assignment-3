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
    "Hyderabad": [("Bangalore", 570), ("Chennai", 630)],
    "Bangalore": [("Hyderabad", 570), ("Chennai", 350), ("Mumbai", 980)],
    "Chennai": [("Hyderabad", 630), ("Bangalore", 350)],
    "Mumbai": [("Bangalore", 980)]
}

start_city = "Hyderabad"
result = dijkstra(graph, start_city)

print("Shortest distances from", start_city)
for city in result:
    print(city, ":", result[city])
