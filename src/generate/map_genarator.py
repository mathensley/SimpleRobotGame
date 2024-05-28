import random

def bfs(grid, start, visited):
    if visited is None:
        visited = set()

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    visited.add(start)

    for direction in directions:
        next_cell = (start[0] + direction[0], start[1] + direction[1])
        if (0 <= next_cell[0] < len(grid) and 
            0 <= next_cell[1] < len(grid[0]) and
            grid[next_cell[0]][next_cell[1]] == '-' and 
            next_cell not in visited):
            bfs(grid, next_cell, visited)

    return len(visited) == sum(row.count('-') for row in grid)

def check_connectivity(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '-':
                return bfs(grid, (i, j), None)
    return True

def add_walls(grid, w):
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    
    while count < w:
        x = random.randint(0, rows - 1)
        y = random.randint(0, cols - 1)
        if x == y == 0:
            continue
        if grid[x][y] == '-':
            grid[x][y] = 'X'
            if not check_connectivity(grid):
                grid[x][y] = '-'
            else:
                count += 1

def add_treasure(grid, t):
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    while count < t:
        x = random.randint(0, rows - 1)
        y = random.randint(0, cols - 1)
        if x == y == 0:
            continue
        if grid[x][y] == '-':
            grid[x][y] = '?'
            count += 1

def generate_rand_map(row, col, w, t):
    grid = [['-' for _ in range(col)] for _ in range(row)]
    add_walls(grid, w)
    add_treasure(grid, t)
    return grid

def print_grid(grid):
    num_cols = len(grid[0])
    header = "   " + "".join(str(col).rjust(2) for col in range(num_cols))
    print(header)
    print("  +" + "--" * num_cols + "-+")
    
    for row_idx, row in enumerate(grid):
        row_str = " ".join(row)
        print(f"{row_idx:2}| {row_str} |")
    
    print("  +" + "--" * num_cols + "-+")