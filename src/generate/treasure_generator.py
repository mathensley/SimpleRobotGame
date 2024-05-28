import math, random
from src import Coord, Treasure

t = {'copper': 1, 'silver': 5, 'gold': 10}

def distribute(coords, grid):
    treasures = []
    copper_prop = math.ceil(len(coords)/2)
    silver_prop = math.ceil((len(coords)/2)/2)
    gold_prop = len(coords) - (copper_prop + silver_prop)

    for _ in range(copper_prop):
        x, y = coords.pop()
        treasures.append(Treasure("copper", t.get('copper'), Coord(x, y)))
        grid[x][y] = 'C'
    for _ in range(silver_prop):
        x, y = coords.pop()
        treasures.append(Treasure("silver", t.get('silver'), Coord(x, y)))
        grid[x][y] = 'S'
    for _ in range(gold_prop):
        x, y = coords.pop()
        treasures.append(Treasure("gold", t.get('gold'), Coord(x, y)))
        grid[x][y] = 'G'
    
    return treasures

def generate_treasures(grid):
    coords = []
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == '?':
                coords.append((x,y))
    random.shuffle(coords)
    return distribute(coords, grid)