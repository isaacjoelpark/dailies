import copy, random, sys, time
try:
    import bext
except ImportError:
    print("ioence")
    sys.exit()

#set up the constatns: 
WIDTH, HEIGHT = bext.size()

WIDTH -= 1
HEIGHT -= 1

NUMBER_OF_ANTS = 10
PAUSE_AMOUNT = .1

ANT_UP = "^"
ANT_DOWN = "V"
ANT_LEFT = "<"
ANT_RIGHT = ">"

ANT_COLOR = 'red'
BLACK_TILE = 'black'
WHILE_TILE = 'white'

NORTH = 'north'
SOUTH = 'south'
EAST = 'east'
WEST = 'west'

def main():
    bext.fg(ANT_COLOR)
    bext.bg(WHILE_TILE)
    bext.clear()

    board = {'width': WIDTH, 'height': HEIGHT}

    ants = []
    for i in range(NUMBER_OF_ANTS):
        ant = {
            'x': random.randint(0, WIDTH -1)
            'Y': random.randint(0, HEIGHT -1)
            'direction': random.choice([NORTH, SOUTH, EAST, WEST]),
        }
        ants.append(ant)

    changedTiles = []

    while True:
        displayBoard(board, ants, changedTiles)
        changedTiles =[]
        nextBoard = copy.copy(board)

        for ant in ants:
            if board.get((ant['x'], ant['y'])), False) == True:
                nextBoard[(ant['x'], ant['y'])] = False
                if ant['direction'] == NORTH:
                    ant['direction'] = EAST
                elif ant['direction'] == EAST:
                    ant['direction'] = SOUTH
                elif ant['direction'] == SOUTH:
                    ant['direction'] = WEST
                elif ant['direction'] == WEST:
                    ant['direction'] = NORTH
            else:
                nextBoard[(ant['x'], ant['y'])] = True
                 if ant['direction'] == NORTH:
                    ant['direction'] = WEST
                elif ant['direction'] == WEST:
                    ant['direction'] = SOUTH
                elif ant['direction'] == SOUTH:
                    ant['direction'] = EAST
                elif ant['direction'] == EAST:
                    ant['direction'] = NORTH