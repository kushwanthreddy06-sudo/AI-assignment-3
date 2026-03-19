import heapq

def astar(grid, start, goal):
    rows, cols = len(grid), len(grid[0])

    pq = [(0, start)]
    g_cost = {start: 0}
    parent = {}

    def heuristic(a, b):
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

        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            nx, ny = x+dx, y+dy

            if 0 <= nx < rows and 0 <= ny < cols:
                if grid[nx][ny] == 1:  
                    continue

                new_cost = g_cost[current] + 1

                if (nx, ny) not in g_cost or new_cost < g_cost[(nx, ny)]:
                    g_cost[(nx, ny)] = new_cost
                    f = new_cost + heuristic((nx, ny), goal)
                    heapq.heappush(pq, (f, (nx, ny)))
                    parent[(nx, ny)] = current

    return None



grid = [[0]*10 for _ in range(10)]
grid[4][5] = 1
grid[5][5] = 1
grid[6][5] = 1

start = (0, 0)
goal = (9, 9)

path = astar(grid, start, goal)
print("Path:", path)
