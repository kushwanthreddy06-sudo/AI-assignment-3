import heapq
import random


def astar(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    open_list = [(0, start)]
    g_cost = {start: 0}
    parent = {}

    def heuristic(a, b):
        return abs(a[0]-b[0]) + abs(a[1]-b[1])

    while open_list:
        _, current = heapq.heappop(open_list)

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

            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:
                new_cost = g_cost[current] + 1

                if (nx, ny) not in g_cost or new_cost < g_cost[(nx, ny)]:
                    g_cost[(nx, ny)] = new_cost
                    f = new_cost + heuristic((nx, ny), goal)
                    heapq.heappush(open_list, (f, (nx, ny)))
                    parent[(nx, ny)] = current

    return None



size = 10
grid = [[0]*size for _ in range(size)]

start = (0, 0)
goal = (9, 9)

current = start
step = 0

print("Starting Navigation...\n")

while current != goal:
    step += 1
    print(f"Step {step}: Current position = {current}")

    
    ox, oy = random.randint(0, size-1), random.randint(0, size-1)
    if (ox, oy) not in [start, goal, current]:
        grid[ox][oy] = 1
        print(f"New obstacle added at: {(ox, oy)}")

    
    path = astar(grid, current, goal)

    if path is None:
        print("No path available! Stopping...")
        break

    print("New path:", path)

    
    if len(path) > 1:
        next_step = path[1]
        current = next_step
    else:
        break

    print()

if current == goal:
    print("\n Goal Reached Successfully!")
else:
    print("\n Could not reach goal.")
