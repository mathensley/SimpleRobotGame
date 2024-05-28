from src import Coord, Robot, utils
from game import match

def start_match_single():
    utils.clear_terminal()
    print("=Single-Player Match=")
    player = Robot("jogador1", 'ª', Coord(0,0))
    match.generate_player(player)

def start_match_ai():
    utils.clear_terminal()
    print("=Robot-AI-Only Match=")
    robot_ai = Robot("WALL-E", 'º', Coord(0,0))
    match.generate_ai(robot_ai)