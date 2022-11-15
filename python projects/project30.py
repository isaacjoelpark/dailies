import sys 
EMPTY_SPACE = '.'
PLAYER_X = 'X'
PLAYER_0 = 'O'

# Note:UPDATE DISPLAYBOARD() & COLUMN LAELS IF BOARD WIDTH IS CHANGED

BOARD_WIDTH = 7
BOARD_HEIGHT = 6 
COLUMN_LABELS = ('1','2','3','4','5','6','7')
assert len(COLUMN_LABELS) == BOARD_WIDTH

def main():
    gameBoard = getNewBoard()
    playerTurn = PLAYER_X
    while True:
        displayBoard(gameBoard)
        playerMove = askForPlayerMove(playerTurn, gameBoard)
        gameBoard[playerMove] = playerTurn

        if isWinner(playerTurn, gameBoard):
            displayBoard(gameBoard)
            print("player " + playerTurn + "haswon!")
            sys.exit()
        elif isFull(gameBoard):
            displayBoard(gameBoard)
            print("there is a tie!")
            sys.exit()

        if playerTurn == PLAYER_X:
            playerTurn = PLAYER_0
        elif playerTurn == PLAYER_0:
            playerTurn = PLAYER_X

def getNewBoard():
    board = {}
    for columnIndex in range(BOARD_WIDTH):
        for rowIndex in range(BOARD_HEIGHT):
            board[(columnIndex, rowIndex)] = EMPTY_SPACE
    return board

def displayBoard(board):
    titleChars = []
    for rowIndex in range(BOARD_HEIGHT):
        for columnIndex in range(BOARD_WIDTH):
            titleChars.append(board[(columnIndex, rowIndex)])
      print("""
        1234567
        +-------+
        |{}{}{}{}{}{}{}|
        |{}{}{}{}{}{}{}|
        |{}{}{}{}{}{}{}|
        |{}{}{}{}{}{}{}|
        |{}{}{}{}{}{}{}|
        |{}{}{}{}{}{}{}|
        +-------+""".format(*tileChars))

def askForPlayerMove(playerTile, board):
    while True:
        print("player {}, enter a column or quite:".format(playerTile))
        response = input('> ').upper().strip()

        if response == 'quit':
            print("thanks for playing")
            sys.exit()
        if response not in COLUMN_LABELS:
            print("enter a number form 1 to {}".format(BOARD_WIDTH))
            continue
        
        columnIndex = int(response)

        if board[(columnIndex, 0)] != EMPTY_SPACE:
            print("THAT CLOUMN IS FULL, SELECT ANOTHER ONE. ")
            continue
        for rowIndex in range(BOARD_HEIGHT-1, -1, -1):
            if board[(columnIndex, rowIndex)] == EMPTY_SPACE:
                return(columnIndex, rowIndex)


def isFull(board):
    for rowIndex in range(BOARD_HEIGHT):
        for columnIndex in range(BOARD_WIDTH):
            if board[(columnIndex, rowIndex)] == EMPTY_SPACE:
                return False
    return True

def isWinner(playerTile):
    for columnIndex in range(BOARD_WIDTH - 3):
        for rowIndex in range(BOARD_HEIGHT):
            tile1 = board[(columnIndex, rowIndex)]
            tile2 = board[(columnIndex + 1, rowIndex)]
            tile3 = board[(columnIndex + 2, rowIndex)]
            tile4 = board[(columnIndex + 3, rowIndex)]
            if tile1 == tile2 == tile3 == tile4 ==  playerTile:
                return True

    for columnIndex in range(BOARD_WIDTH):
        for rowIndex in range(BOARD_HEIGHT - 3):
 # Check for vertical four-in-a-row going down:
            tile1 = board[(columnIndex, rowIndex)]
            tile2 = board[(columnIndex, rowIndex + 1)]
            tile3 = board[(columnIndex, rowIndex + 2)]
            tile4 = board[(columnIndex, rowIndex + 3)]
            if tile1 == tile2 == tile3 == tile4 == playerTile:
                return True

    for columnIndex in range(BOARD_WIDTH - 3):
        for rowIndex in range(BOARD_HEIGHT - 3):
# Check for four-in-a-row going right-down diagonal:
            tile1 = board[(columnIndex, rowIndex)]
            tile2 = board[(columnIndex + 1, rowIndex + 1)]
            tile3 = board[(columnIndex + 2, rowIndex + 2)]
            tile4 = board[(columnIndex + 3, rowIndex + 3)]
            if tile1 == tile2 == tile3 == tile4 == playerTile:
                return True

 # Check for four-in-a-row going left-down diagonal:
            tile1 = board[(columnIndex + 3, rowIndex)]
            tile2 = board[(columnIndex + 2, rowIndex + 1)]
            tile3 = board[(columnIndex + 1, rowIndex + 2)]
            tile4 = board[(columnIndex, rowIndex + 3)]
            if tile1 == tile2 == tile3 == tile4 == playerTile:
                return True
    return False


 # If the program is run (instead of imported), run the game:
 if __name__ == '__main__':
    main()