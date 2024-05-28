from src import Map
from src import generate_rand_map, generate_treasures
from src.enemy.a_star_ai import *
from src import utils

def generate_player(player):
    grid = generate_rand_map(10, 10, 50, 4)
    treasures = generate_treasures(grid)
    choosen_map = Map(grid, player, treasures)
    choosen_map.grid[0][0] = player.shape
    utils.print_grid(choosen_map.grid)
    print(choosen_map.robot)
    player_loop(True, choosen_map)
    utils.clear_terminal()
    utils.print_grid(choosen_map.grid)
    print(f"{choosen_map.robot} - Treasure found: {choosen_map.robot.treasures}")
    print(f"Score: {choosen_map.robot.score}")
    print("Match is over!")

def player_loop(match, choosen_map):
    while match:
        moviment = input("Type 'up', 'down', 'left' or 'right' to move the robot: ")
        if moviment == 'up':
            choosen_map.robot.move_up(choosen_map)
        elif moviment == 'down':
            choosen_map.robot.move_down(choosen_map)
        elif moviment == 'left':
            choosen_map.robot.move_left(choosen_map)
        elif moviment == 'right':
            choosen_map.robot.move_right(choosen_map)
        else:
            print('Invalid input')
            continue
        utils.clear_terminal()
        utils.print_grid(choosen_map.grid)
        print(f"{choosen_map.robot} - Treasure found: {choosen_map.robot.treasures}")
        print(f"Score: {choosen_map.robot.score}")
        choosen_map.check_treasure()
        if len(choosen_map.treasures) == 0:
            match = False

def generate_ai(robot_ai):
    grid = generate_rand_map(10, 10, 50, 4)
    treasures = generate_treasures(grid)
    choosen_map = Map(grid, robot_ai, treasures)
    choosen_map.grid[0][0] = robot_ai.shape
    utils.print_grid(choosen_map.grid)
    print(choosen_map.robot)
    robot_ai_loop(True, choosen_map)
    utils.clear_terminal()
    utils.print_grid(choosen_map.grid)
    print(f"{choosen_map.robot} - Treasure found: {choosen_map.robot.treasures}")
    print(f"Score: {choosen_map.robot.score}")
    print("Match is over!")


def robot_ai_loop(match, choosen_map):
    while match:
        start = choosen_map.robot.coord.as_tuple()
        t = find_closest_treasure(choosen_map, start)
        end = t.coord.as_tuple()
        full_path, _ = a_star(choosen_map.grid, start, end)
        path = reconstruct_path(full_path, start, end) # Coord object
        path.pop()
        while path:
            print(f"Path (inverted): {path}")
            input(f"({choosen_map.robot.name}) will move, please press [enter]. ")
            moviment = (path.pop() - choosen_map.robot.coord).as_tuple()
            if moviment == (-1, 0):
                choosen_map.robot.move_up(choosen_map)
            elif moviment == (1, 0):
                choosen_map.robot.move_down(choosen_map)
            elif moviment == (0, -1):
                choosen_map.robot.move_left(choosen_map)
            elif moviment == (0, 1):
                choosen_map.robot.move_right(choosen_map)
            else:
                print("Invalid input")
            utils.clear_terminal()
            utils.print_grid(choosen_map.grid)
            print(f"{choosen_map.robot} - Treasure found: {choosen_map.robot.treasures}")
            print(f"Score: {choosen_map.robot.score}")
            choosen_map.check_treasure()
        if len(choosen_map.treasures) == 0:
            match = False

def find_closest_treasure(choosen_map, start):
    treasures = choosen_map.treasures
    closest_treasure = None
    min_dist = float('inf')
    for treasure in treasures:
        dist = heuristic(start, treasure.coord.as_tuple())
        if dist < min_dist:
            closest_treasure = treasure
            min_dist = dist
    return closest_treasure