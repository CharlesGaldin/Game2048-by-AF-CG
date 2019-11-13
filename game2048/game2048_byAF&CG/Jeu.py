from grid_2048 import *
from textual_2048 import *
from themes import *

grid = init_game()
print(grid_to_string_with_size(grid))
move = read_player_command()

if move=='z':
    grid = move_grid()

