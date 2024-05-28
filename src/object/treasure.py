class Treasure:
    def __init__(self, name, value, coord):
        self.name = name
        self.value = value
        self.coord = coord
    
    def __repr__(self):
        return f"({self.coord}) {self.name} = {self.value}"