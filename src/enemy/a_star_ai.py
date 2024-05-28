import heapq
from src import Coord

# Manhattam distance
def heuristic(a, b):
    x1, y1 = a
    x2, y2 = b
    return abs(x1 - x2) + abs(y1 - y2)

def neighbors(grid, node):
    result = []
    for d in [(0,1), (1,0), (0, -1), (-1, 0)]:
        neighbor = (node[0] + d[0], node[1] + d[1])
        if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]) and grid[neighbor[0]][neighbor[1]] != 'X':
            result.append(neighbor)
    return result

def a_star(grid, start, end):
    pq = [(0, start)]
    path = {start: None}
    cost = {start: 0}
    
    while pq:
        cp, current = heapq.heappop(pq)
        if current == end:
            break
        for next in neighbors(grid, current):
            new_cost = cost[current] + 1
            if next not in cost or new_cost < cost[next]:
                cost[next] = new_cost
                p = new_cost + heuristic(end, next)
                heapq.heappush(pq, (p, next))
                path[next] = current
    return path, cost

def reconstruct_path(path, start, end):
    current = end
    reversed_path = []
    while current != start:
        #reversed_path.append(current)
        #current = path[current]
        reversed_path.append(Coord(current[0], current[1]))
        current = path[current]
    #reversed_path.append(start)
    reversed_path.append(Coord(start[0], start[1]))
    #reversed_path.reverse()
    return reversed_path