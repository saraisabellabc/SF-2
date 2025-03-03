import random
def tileLabels(n): 
    lst = []
    for i in range(1, n**2 -1):
        lst.append(str(i))
    lst.append('  ')
    return lst 
'''
def getNewPuzzle(n):
    puzzle = []
    tiles = tileLabels(n)
    random.shuffle(tiles)
    for i in range(0, n):
        sublist = []
        for j in range(0, n):  
            sublist.append(tiles[j])
            if len(sublist[j]) == 1:
                sublist[j] += ' '            
        puzzle.append(sublist)

    print(puzzle)
    return puzzle

getNewPuzzle(3)
'''
#There is a problem with the code, it gives back the same sublist

def findEmptyFile(puzzle):
    for i in range(len(puzzle)):
        for j in range(len(puzzle)):
            if '  ' == puzzle[i][j] :
                return(i, j)

'''
def nextMov(puzzle):
    empty = findEmptyPuzzle(puzzle)
    move = input('Chose between W A D S:')
    if move == 'W':
    if move == 'A':
    if move == 'D'
'''
#didnt finish

        
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

