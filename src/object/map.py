class Map:
    def __init__(self, grid, robot, treasures):
        self.grid = grid
        self.robot = robot
        self.treasures = treasures
        self.max_rows = len(grid)
        self.max_cols = len(grid[0])
    
    def is_valid_mov(self, coord):
        return (0 <= coord.x < self.max_rows and 0 <= coord.y < self.max_cols) and (self.grid[coord.x][coord.y] != 'X')
    
    def check_treasure(self):
        for treasure in self.treasures:
            if self.robot.coord == treasure.coord:
                print(f"({self.robot.name}) found treasure: {treasure}")
                self.update_robot_status(treasure)
                self.treasures.remove(treasure)
    
    def update_robot_status(self, treasure):
        self.robot.treasures.append(treasure)
        self.robot.score += treasure.value