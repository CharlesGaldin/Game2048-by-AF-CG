import random
import numpy as np

def create_grid():
    s = []
    for _ in range(0,4):
        s.append([0,0,0,0])
    return s

def grid_add_new_tile_at_position(game_grid,x,y):
    p = random.random()
    if p > 0.9:
        game_grid[x][y] = 4
    else:
        game_grid[x][y] = 2
    return game_grid

def get_empty_tiles_positions(game_grid):
    pos = []
    for i in range(4):
        for j in range(4):
            if game_grid[i][j] == ' ' or game_grid[i][j] == 0:
                pos.append((i,j))
    return pos

def get_new_position(game_grid):
    li = get_empty_tiles_positions(game_grid)
    new = random.choice(li)
    return new[0],new[1]

def add_new_tile(game_grid):
    x,y = get_new_position(game_grid)
    game_grid = grid_add_new_tile_at_position(game_grid,x,y)
    return game_grid

def init_game():
    g = create_grid()
    for _ in range(2):
        g = add_new_tile(g)
    return g


def grid_to_string(game_grid):
    s = ""
    for i in range(4):
        s+= " === === === ===\n"
        for j in range(4):
            s+='|'
            s+= ' {} '.format(game_grid[i][j])
        s+= '|\n'
    s+= " === === === ===\n"
    return s

def long_value(grid):
    m = 1
    for i in range(4):
        for j in range(4):
            if len(str(grid[i][j])) > m:
                m = len(str(grid[i][j]))
    return m

def grid_to_string_with_size(grid):
    size = long_value(grid)+2
    s = ""
    for i in range(4):
        toit = '='*size
        s+= ' '+toit+' '+toit+' '+toit+' '+toit+'\n'
        for j in range(4):
            count = 0
            s+='| '
            s+= '{}'.format(grid[i][j])
            count += 1 + len(str(grid[i][j]))
            while count < size:
                s+=' '
                count +=1
            count = 0
        s+= '|\n'
    s+= ' '+toit+' '+toit+' '+toit+' '+toit+'\n'
    return s




def move_row_left(row):
    n = len(row)
    fusions = [] #liste des endroits ou on a fait une fusion (on ne peut pas en faire plus d'une par case)
    for i in range(1,n):
        j = i-1
        while j>=0 and row[j] in [' ',0]: #on trouve la premiere case occupée à gauche de i, ou -1 sinon
            j-=1
        if j == -1:
            row[0] = row[i]
            row[i] = 0
        elif row[j] == row[i] and j not in fusions: # FUSION
            row[j] = row[j] + row[i]
            row[i] = 0
            fusions.append(j)
        else: #pas de fusion
            if j+1!=i: #sinon il n'ya rien a faire
                row[j+1] = row[i]
                row[i] = 0

    return row

def move_row_right(row):
    row2 = row[::-1] #reverse
    row2 = move_row_left(row2)
    return row2[::-1]


def move_grid(grid,d):
    n = len(grid)
    if d == 'left':
        for i in range(n):
            grid[i] = move_row_left(grid[i])
    elif d == 'right':
        for i in range(n):
            grid[i] = move_row_right(grid[i])
    elif d == 'up':
        grid = np.transpose(grid)
        for i in range(n):
            grid[i] = move_row_left((grid[i]))
        grid = np.transpose(grid).tolist()
    elif d == 'down':
        grid = np.transpose(grid)
        for i in range(n):
            grid[i] = move_row_right(grid[i])
        grid = np.transpose(grid).tolist()
    return grid


def is_grid_full(grid):
    n = len(grid[0])
    for i in range(n):
        for j in range(n):
            if grid[i][j] in [0,' ']:
                return False
    return True

#print(is_grid_full([[2, 2, 2, 2], [4, 8, 8, 16], [1, 8, 1, 4], [4, 8, 16, 32]]))


def move_possible(grid):
    res = [True,True,True,True]
    if move_grid(grid,'left') == grid:
        res[0] = False
    if move_grid(grid,'right') == grid:
        res[1] = False
    if move_grid(grid,'up') == grid:
        res[2] = False
    if move_grid(grid,'down') == grid:
        res[3] = False

def is_game_over(grid):
    return is_grid_full(grid) and move_possible(grid) == [False,False,False,False]

def get_grid_tile_max(grid):
    n = len(grid[0])
    m = 0
    for i in range(n):
        for j in range(n):
            if grid[i][j] > m:
                m = grid[i][j]
    return m



    

    

                




