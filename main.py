import random

row = 3
column = 3
choiceList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
youWon = 'You won!'
computerWon = 'The computer won!'
draw = 'This is a draw!'

'''
- - -
- - -
- - -

1 2 3
4 5 6
7 8 9
'''
board2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def printModeTwoBoard(board):
    
    for index in range(0, 9):
        if index % 3 == 0:
            print()
        print(board[index], end=' ')


def emptyBoard(board):
    for index in range(0, 9):
        board.append('-')


def playerChoiceInput():
    print()
    return int(input('Enter a number from 1-9: '))


def AIChoice():
    return random.choice(board2)


def isEmptyPile(board, choice):
    # return True if the pile chosen is empty, return False otherwise
    if board[choice - 1] == '-':
        return True
    return False


def fullBoard2(board):
    # return False if the pile is empty, return True otherwise
    for num in range(len(board)):
        if board[num] == '-':
            return False
    return True


def gameResult2(board, yourSymbol, computerSymbol):
    # row check
    if board[0] == yourSymbol and board[1] == yourSymbol and board[2] == yourSymbol:
        return 'you win'
    elif board[0] == computerSymbol and board[1] == computerSymbol and board[2] == computerSymbol:
        return 'computer win'

    elif board[3] == yourSymbol and board[4] == yourSymbol and board[5] == yourSymbol:
        return 'you win'
    elif board[3] == computerSymbol and board[4] == computerSymbol and board[5] == computerSymbol:
        return 'computer win'

    elif board[6] == yourSymbol and board[7] == yourSymbol and board[8] == yourSymbol:
        return 'you win'
    elif board[6] == computerSymbol and board[7] == computerSymbol and board[8] == computerSymbol:
        return 'computer win'

    # column check
    elif board[0] == yourSymbol and board[3] == yourSymbol and board[6] == yourSymbol:
        return 'you win'
    elif board[0] == computerSymbol and board[3] == computerSymbol and board[6] == computerSymbol:
        return 'computer win'

    elif board[1] == yourSymbol and board[4] == yourSymbol and board[7] == yourSymbol:
        return 'you win'
    elif board[1] == computerSymbol and board[4] == computerSymbol and board[7] == computerSymbol:
        return 'computer win'

    elif board[2] == yourSymbol and board[5] == yourSymbol and board[8] == yourSymbol:
        return 'you win'
    elif board[2] == computerSymbol and board[5] == computerSymbol and board[8] == computerSymbol:
        return 'computer win'

    # diagonal check
    elif board[0] == yourSymbol and board[4] == yourSymbol and board[8] == yourSymbol:
        return 'you win'
    elif board[0] == computerSymbol and board[4] == computerSymbol and board[8] == computerSymbol:
        return 'computer win'

    elif board[2] == yourSymbol and board[4] == yourSymbol and board[6] == yourSymbol:
        return 'you win'
    elif board[2] == computerSymbol and board[4] == computerSymbol and board[6] == computerSymbol:
        return 'computer win'


    elif fullBoard2(board):
        return 'draw'


def playModeTwo():
    # the player has to select a number from 1-9 to play the game
    board = []
    emptyBoard(board)
    printModeTwoBoard(board)

    print()
    yourSymbol = input('Do you want to use \'O\' or \'X\'?')
    if yourSymbol == 'O':
        computerSymbol = 'X'
    else:
        computerSymbol = 'O'

    while True:
        while True:
            yourChoice = playerChoiceInput()
            if isEmptyPile(board, yourChoice):
                board[yourChoice - 1] = yourSymbol
                break
            print('The pile is filled already! Please try another number!')

        while True:
            if fullBoard2(board):
                break
            computerChoice = AIChoice()
            if isEmptyPile(board, computerChoice):
                board[computerChoice - 1] = computerSymbol
                break

        if gameResult2(board, yourSymbol, computerSymbol) == 'you win':
            printModeTwoBoard(board)
            print()
            return 'You won!'

        elif gameResult2(board, yourSymbol, computerSymbol) == 'computer win':
            printModeTwoBoard(board)
            print()
            return 'AI won!'

        elif gameResult2(board, yourSymbol, computerSymbol) == 'draw':
            printModeTwoBoard(board)
            print()
            return 'Draw!'


        else:
            printModeTwoBoard(board)


def gameResult(board, playerChoice, computerChoice):
    # prints the result of the game
    youWon = 'You won!'
    computerWon = 'The computer won!'

    for i in range(0, row):
        if board[i][0] == playerChoice and board[i][1] == playerChoice and board[i][2] == playerChoice:
            print(youWon)
        if board[i][0] == computerChoice and board[i][1] == computerChoice and board[i][2] == computerChoice:
            print(computerWon)

    for j in range(0, column):
        if board[0][j] == playerChoice and board[1][j] == playerChoice and board[2][j] == playerChoice:
            print(youWon)
        if board[0][j] == computerChoice and board[1][j] == computerChoice and board[2][j] == computerChoice:
            print(computerWon)

    if (board[0][0] == playerChoice and board[1][1] == playerChoice and board[2][2] == playerChoice) or \
            (board[2][0] == playerChoice and board[1][1] == playerChoice and board[0][2] == playerChoice):
        print(youWon)

    if (board[0][0] == computerChoice and board[1][1] == computerChoice and board[2][2] == computerChoice) or \
            (board[2][0] == computerChoice and board[1][1] == computerChoice and board[0][2] == computerChoice):
        print(computerWon)

    for i in range(0, row):
        for j in range(0, column):
            if board[i][j] == '-':
                continue

    return True


def modified_board(board, rowNo, colNo, choice):
    for i in range(0, row):
        for j in range(0, column):
            choice = board[rowNo - 1][colNo - 1] = choice


def new_board():
    # create an empty board
    rowList = []
    for i in range(0, row):
        columnList = []
        for j in range(0, column):
            columnList.append('-')
        rowList.append(columnList)
    return rowList


def print_board(board):
    # display the board
    for i in range(0, row):
        for j in range(0, column):
            print(board[i][j], end=' ')
        print()


def gameEnd(board):
    # return True if the game ends, returns False otherwise
    for i in range(0, row):
        if (board[i][0] == 'X' and board[i][1] == 'X' and board[i][2] == 'X') or \
                (board[i][0] == 'O' and board[i][1] == 'O' and board[i][2] == 'O'):
            return True
    # checking for row

    for j in range(0, column):
        if (board[0][j] == 'X' and board[1][j] == 'X' and board[2][j] == 'X') or \
                (board[0][j] == 'O' and board[1][j] == 'O' and board[2][j] == 'O'):
            return True
    # checking for column

    if (board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X') or \
            (board[2][0] == 'X' and board[1][1] == 'X' and board[0][2] == 'X') or \
            (board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O') or \
            (board[2][0] == 'O' and board[1][1] == 'O' and board[0][2] == 'O'):
        return True
    # checking for diagonal

    for i in range(0, row):
        for j in range(0, column):
            if board[i][j] == '-':
                return False
    # check if the board is full or not

    return True


def fullBoard(board):
    for i in range(0, row):
        for j in range(0, column):
            if board[i][j] == '-':
                return False
    return True


def pileChosen(board, givenRow, givenCol):
    # returns true if the chosen row and column is chosen, return false otherwise
    for i in range(0, row):
        for j in range(0, column):
            if board[givenRow - 1][givenCol - 1] != '-':
                return True
    return False


def emptyBoard(board):
    for index in range(0, 9):
        board.append('-')


def playModeOne():
    # the mode where the players choose the row and column to play the game
    board = new_board()
    print_board(board)

    while True:
        playerChoice = (input('Pick "O" or "X"'))

        if playerChoice == 'O' or playerChoice == 'X':
            break
        else:
            print('Pick "O" or "X" only ')

    if playerChoice == 'O':
        computerChoice = 'X'

    else:
        computerChoice = 'O'

    while True:
        playerTurn = input('Do you want to go first?[y/n]')
        if playerTurn == 'y' or playerTurn == 'n':
            break
        else:
            print('Pick "y" or "n" only ')

    if playerTurn == 'y':
        computerTurn = False

    else:
        computerTurn = True

    while not gameEnd(board):
        if computerTurn:

            computerRow = random.choice([1, 2, 3])
            computerCol = random.choice([1, 2, 3])
            while pileChosen(board, computerRow, computerCol):
                computerRow = random.choice([1, 2, 3])
                computerCol = random.choice([1, 2, 3])
            modified_board(board, computerRow, computerCol, computerChoice)
            print('Computer Turn')

        else:
            print('Your Turn')
            while True:
                try:
                    playerRow = int(input('Pick a row[1-3]:'))
                except ValueError:
                    playerRow = -1
                if playerRow in [1, 2, 3]:
                    break

            while True:
                try:
                    playerCol = int(input('Pick a column[1-3]:'))
                except ValueError:
                    playerCol = -1
                if playerCol in [1, 2, 3]:
                    break

            while pileChosen(board, playerRow, playerCol):
                while True:
                    try:
                        playerRow = int(input('Pick a row[1-3]:'))
                    except ValueError:
                        playerRow = -1
                    if playerRow in [1, 2, 3]:
                        break

                while True:
                    try:
                        playerCol = int(input('Pick a column[1-3]:'))
                    except ValueError:
                        playerCol = -1
                    if playerCol in [1, 2, 3]:
                        break

            modified_board(board, playerRow, playerCol, playerChoice)

        print_board(board)
        gameResult(board, playerChoice, computerChoice)
        if fullBoard(board):
            print(draw)

        if computerTurn:
            computerTurn = False
        else:
            computerTurn = True


def rules():
    print('Mode one is using a two dimensional array and the users or players have to input the rows and columns')
    print('Mode two is using a two dimensional array and the users or players have to input numbers from 1-9')


def welcome():
    print('Welcome Tic Tac Toe Game')

    while True:

        print('1 = rules \t 2 = mode one \t 3 = mode two')
        try:
            menu = int(input())
        except ValueError:
            menu = -1
        if menu == 1:
            rules()
        elif menu == 2:
            playModeOne()
            break
        elif menu == 3:
            print()
            print(playModeTwo())
            break
        else:
            continue


if __name__ == '__main__':
    welcome()
