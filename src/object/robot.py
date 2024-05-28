from src import Coord

class Robot:
    def __init__(self, name, shape, coord):
        self.name = name
        self.coord = coord
        self.shape = shape
        self.treasures = []
        self.score = 0

    def move_up(self, map_obj):
        if map_obj.is_valid_mov(Coord(self.coord.x-1, self.coord.y)):
            map_obj.grid[self.coord.x][self.coord.y] = '-'
            self.coord.x = self.coord.x - 1
            map_obj.grid[self.coord.x][self.coord.y] = self.shape
    
    def move_down(self, map_obj):
        if map_obj.is_valid_mov(Coord(self.coord.x+1, self.coord.y)):
            map_obj.grid[self.coord.x][self.coord.y] = '-'
            self.coord.x = self.coord.x + 1
            map_obj.grid[self.coord.x][self.coord.y] = self.shape
    
    def move_left(self, map_obj):
        if map_obj.is_valid_mov(Coord(self.coord.x, self.coord.y-1)):
            map_obj.grid[self.coord.x][self.coord.y] = '-'
            self.coord.y = self.coord.y - 1
            map_obj.grid[self.coord.x][self.coord.y] = self.shape
    
    def move_right(self, map_obj):
        if map_obj.is_valid_mov(Coord(self.coord.x, self.coord.y+1)):
            map_obj.grid[self.coord.x][self.coord.y] = '-'
            self.coord.y = self.coord.y + 1
            map_obj.grid[self.coord.x][self.coord.y] = self.shape
    
    def __repr__(self):
        return f"({self.name}) {self.coord}"