import random
import sys
def tileLabels(n): 
    lst = []
    for i in range(1, n**2 ):
        lst.append(str(i))
    lst.append('  ')
    return lst 

def getNewPuzzle(n):
    puzzle = []

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
        puzzle.append(sublist)

    return puzzle




def findEmptyTile(puzzle):
    for row in range(len(puzzle)):
        for column in range(len(puzzle[row])):
            if '  ' == puzzle[row][column] :
                return row, column



def nextMove(puzzle):
    row, col = findEmptyTile(puzzle)
    n = len(puzzle)
    valid_moves = {}
    
    if row > 0:
        valid_moves['W'] = '(W)'
    if row < n - 1:
        valid_moves['S'] = '(S)'
    if col > 0:
        valid_moves['A'] = '(A)'
    if col < n - 1:
        valid_moves['D'] = '(D)'
    
    while True:
        displayBoard(puzzle)
        move_list = []
        for i in ['W','A', 'S', 'D']:
            move_list.append(valid_moves.get(i, '( )'))
        move_input = move_list
        print(f"                          {move_input[0]}")
        answer_input = input(f"Enter WASD (or QUIT): {' '.join(move_input[1:])} \n").strip().upper()
        print(str(answer_input))

        
        
        if answer_input == "QUIT":
            print("Game stopped")
            sys.exit() 
        elif answer_input in valid_moves:
            return answer_input
        else:
            print("Does not work. Try again.")

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


n = int(input("Enter the size of the puzzle (n x n): "))
puzzle = getNewPuzzle(n)
nextMove(puzzle)  
    
