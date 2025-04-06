# Sara Isabella Barajas-Cruz
# 2443227
# Course: 420-SF2-RE - Data Structures and Object Oriented Programming

import random
import sys

# 1. returns list of strings (numbers 1 to n**2-1)
def tileLabels(n): 
    lst = []
    for i in range(1, n**2 ):
        lst.append(str(i))
    lst.append('  ')
    return lst 

# 2. nested loop, returns the board (board of tiles)
def getNewPuzzle(n):
    board = []

    tiles = tileLabels(n)
    random.shuffle(tiles)

    index = 0
    for i in range(0, n):
        sublist = []
        for j in range(0, n):  
            if index < len(tiles):
                sublist.append(tiles[index])
                index += 1
            if len(sublist[j]) == 1:
                sublist[j] += ' '           
        board.append(sublist)

    return board


# 3. returns the row and column of the empty tile
def findEmptyTile(board):
    for row in range(len(board)):
        for column in range(len(board[row])):
            if '  ' == board[row][column] :
                return row, column



# 4. returns the command of the user (input)
def nextMove(board):
    row, col = findEmptyTile(board)
    n = len(board)
    valid_moves = {}
    
    if row < n - 1:
        valid_moves['W'] = '(W)'  # Move tile UP (empty space moves DOWN)
    if row > 0:
        valid_moves['S'] = '(S)'  # Move tile DOWN (empty space moves UP)
    if col < n - 1:
        valid_moves['A'] = '(A)'  # Move tile LEFT (empty space moves RIGHT)
    if col > 0:
        valid_moves['D'] = '(D)'  # Move tile RIGHT (empty space moves LEFT)
        
    while True:
        move_list = []
        for i in ['W','A', 'S', 'D']:
            move_list.append(valid_moves.get(i, '( )'))
        print(f"                          {move_list[0]}")
        answer_input = input(f"Enter WASD (or QUIT): {' '.join(move_list[1:])} \n").strip().upper()

        
        if answer_input == "QUIT":
            print("Game stopped")
            sys.exit() 
        elif answer_input in valid_moves:
            return answer_input
        else:
            print("Does not work. Try again.")

# 5. updates the board 
def makeMove(board, move):
    row_empty, col_empty = findEmptyTile(board)

    if move == 'W' and row_empty < len(board) - 1:  
        board[row_empty][col_empty], board[row_empty + 1][col_empty] = board[row_empty + 1][col_empty], board[row_empty][col_empty]
    elif move == 'S' and row_empty > 0:  
        board[row_empty][col_empty], board[row_empty - 1][col_empty] = board[row_empty - 1][col_empty], board[row_empty][col_empty]
    elif move == 'A' and col_empty < len(board[0]) - 1: 
        board[row_empty][col_empty], board[row_empty][col_empty + 1] = board[row_empty][col_empty + 1], board[row_empty][col_empty]
    elif move == 'D' and col_empty > 0:  
        board[row_empty][col_empty], board[row_empty][col_empty - 1] = board[row_empty][col_empty - 1], board[row_empty][col_empty]

# to display the board
def displayBoard(board_lst):
    n = len(board_lst)

    labels = []
    for i in range(n):
        for j in range(n):
            labels.append(board_lst[i][j])

    draw_board = ''
    horizontal_div = ('+' + '------')*n + '+'
    vertical_div = '|' + ' '*6
    vertical_label = '|' + ' '*2 + '{}' + ' '*2
    
    for i in range(n):
        draw_board = draw_board + horizontal_div +'\n'+\
                    vertical_div*n + '|\n' + \
                    vertical_label*n + '|\n'+\
                    vertical_div*n + '|\n'
    draw_board += horizontal_div
    print(draw_board.format(*labels))


# 6. verify if its solved
def verifySolved(board):
    size = len(board)  # Use 'size' instead of 'len'
    
    for i in range(size):
        for j in range(size - 1):
            if board[i][j] != '  ' and board[i][j + 1] != '  ' and int(board[i][j]) > int(board[i][j + 1]):
                return False  # Ensures row-wise order

    for j in range(size):
        for i in range(size - 1):
            if board[i][j] != '  ' and board[i + 1][j] != '  ' and int(board[i][j]) > int(board[i + 1][j]):
                return False  # Ensures column-wise order

    return True


# 6 main program (to run the game)
def main():
    print('Welcome to the Sliding Puzzle game! \n The objective is to obtain an increasing sorted order of the tiles from left to right and top to bottom by continuously sliding the tiles. Tiles can only slide to an adjacent empty cell. Possible valid moves are: left, right, up, down. \n Your instructions are very simple: \n 1. Enter the size of your board. A display of your board will be shown. \n 2. Enter the move you want to do : \n Entering W, means a tile is moved up into the empty tile \n Entering A, means a tile is moved left into the empty tile \n Entering D, means a tile is moved right into the empty tile. \n Entering S, means a tile is moved down into the empty tile')
    n = int(input("Enter the size of the board (n x n), must be greater than 2: "))
    board = getNewPuzzle(n)
    turns = 0
    max_turns = 31 if n == 3 else 80
    
    
    while turns < max_turns:
        displayBoard(board)
        if verifySolved(board):
            print(f"Congratulations! You solved the puzzle in {turns} moves!")
            sys.exit()
        
        move = nextMove(board)
        makeMove(board, move)
        turns += 1
    
    print("Best of luck next time!")

main()