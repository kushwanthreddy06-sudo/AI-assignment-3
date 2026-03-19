import heapq
import random

def astar(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    pq = [(0, start)]
    g = {start: 0}

    def h(a, b):
        return abs(a[0]-b[0]) + abs(a[1]-b[1])

    while pq:
        _, current = heapq.heappop(pq)

        if current == goal:
            return True

        x, y = current

        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx, ny = x+dx, y+dy

            if 0 <= nx < rows and 0 <= ny < cols:
                if grid[nx][ny] == 0:
                    new_cost = g[current] + 1
                    if (nx, ny) not in g or new_cost < g[(nx, ny)]:
                        g[(nx, ny)] = new_cost
                        heapq.heappush(pq, (new_cost + h((nx, ny), goal), (nx, ny)))

    return False



grid = [[0]*10 for _ in range(10)]

start = (0, 0)
goal = (9, 9)
current = start

while current != goal:
    print("Current:", current)

    
    ox, oy = random.randint(0,9), random.randint(0,9)
    grid[ox][oy] = 1

    
    if not astar(grid, current, goal):
        print("No path! Replanning...")
        continue

    
    x, y = current
    if x < goal[0]:
        next_step = (x+1, y)
    elif y < goal[1]:
        next_step = (x, y+1)
    else:
        break

    if grid[next_step[0]][next_step[1]] == 1:
        print("Obstacle ahead! Replanning...")
        continue

    current = next_step

print("Reached goal!")
