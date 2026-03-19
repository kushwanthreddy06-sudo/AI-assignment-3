import heapq
import random


def generate_grid(size, density):
    grid = [[0 for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for j in range(size):
            if random.random() < density:
                grid[i][j] = 1
    return grid

def astar(grid, start, goal):
    size = len(grid)
    pq = [(0, start)]
    g = {start: 0}
    parent = {}

    def h(a, b):
        return abs(a[0]-b[0]) + abs(a[1]-b[1])

    while pq:
        _, current = heapq.heappop(pq)

        if current == goal:
            path = []
            while current in parent:
                path.append(current)
                current = parent[current]
            path.append(start)
            return path[::-1]

        x, y = current

        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx, ny = x+dx, y+dy

            if 0 <= nx < size and 0 <= ny < size:
                if grid[nx][ny] == 1:
                    continue

                new_cost = g[current] + 1
                if (nx, ny) not in g or new_cost < g[(nx, ny)]:
                    g[(nx, ny)] = new_cost
                    f = new_cost + h((nx, ny), goal)
                    heapq.heappush(pq, (f, (nx, ny)))
                    parent[(nx, ny)] = current

    return None


size = 70
density = 0.2   

grid = generate_grid(size, density)

start = (0, 0)
goal = (69, 69)

grid[0][0] = 0
grid[69][69] = 0

path = astar(grid, start, goal)

if path:
    print("Path found! Length:", len(path))
else:
    print("No path found")
