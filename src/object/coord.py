class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def as_tuple(self):
        return (self.x, self.y)
    
    def __sub__(self, other):
        if isinstance(other, Coord):
            return Coord(self.x - other.x, self.y - other.y)
        raise ValueError("Subtraction only between Coord objects.")

    def __repr__(self):
        return f"<{self.x}, {self.y}>"
    
    def __eq__(self, other):
        if isinstance(other, Coord):
            return self.x == other.x and self.y == other.y
        return False
    
    def __hash__(self):
        return hash((self.x, self.y))