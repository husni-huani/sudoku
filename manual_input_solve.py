from class_sudoku import sudoku_board
from time import time

print('Input 9x9 sudoku board\n')
board = []

for i in range(9):
    str_input = input()
    list_str = str_input.split(' ')
    list_num = []
    for element in list_str:
        list_num.append(int(element))
    board.append(list_num)

start = time()
print()
sudoku = sudoku_board(board)
print('Solved sudoku : ')
sudoku.solve()
print('\nElapsed time : ', time()- start)
    