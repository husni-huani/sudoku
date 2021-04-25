def board_to_num(board):
    num = 0
    for row in range(9):
        for column in range(9):
            num = (num << 4) + board[row][column]
    return num

def num_to_board(num):
    board = [[0 for i in range(9)] for i in range(9)]
    for row in range(9):
        for column in range(9):
            pos = (8-row)*36 + (8-column)*4
            curr_val = (num >> pos) & 15
            board[row][column] = curr_val
    return board

class sudoku_board():
    def __init__(self, board):
        self.num_board = board_to_num(board)
        # sudoku board direpresentasikan menjadi suatu integer 324 bit
        self.solution = 0

    def show_board(self):
        board = num_to_board(self.num_board)
        str_show = ''
        for row in range(9):
            for column in range(9):
                str_show += str(board[row][column]) + ' '
            str_show += '\n'
        print(str_show)

    def val_index(self, row, column):
        # Memberikan nilai pada suatu board
        pos = (8-row)*36 + (8-column)*4
        return (self.num_board >> pos) & 15
    
    def change_block(self, row, column, num):
        # mengubah nilai pada suatu board
        pos = (8-row)*36 + (8-column)*4
        back = self.num_board & ((1 << (pos)) -1)
        front = self.num_board >> (pos+4)
        self.num_board = (((front << 4) + num) << pos) + back
        
    def is_valid_num(self, row, column, num):
        # check row
        for j in range(9):
            if num == self.val_index(row,j):
                return False
        # check column
        for i in range(9):
            if num == self.val_index(i, column):
                return False
        # check section
        index_i = (row // 3)*3
        index_j = (column // 3)*3
        for add_i in range(3):
            for add_j in range(3):
                if num == self.val_index(index_i+add_i,index_j+add_j):
                    return False
        return True

    def possible_num(self, row, column):
        # Mengecek angka yang mungkin untuk suatu kotak kosong
        if self.val_index(row, column) != 0:
            return []
        ans = (1 << 9) -1
        for j in range(9):
            if self.val_index(row, j) != 0:
                pos = 9-self.val_index(row, j)
                back = ans & ((1 << (pos)) -1)
                front = ans >> (pos+1)
                ans = (front << (pos+1)) + back
        for i in range(9):
            if self.val_index(i, column) != 0:
                pos = 9-self.val_index(i, column)
                back = ans & ((1 << (pos)) -1)
                front = ans >> (pos+1)
                ans = (front << (pos+1)) + back 
        index_i = (row // 3)*3
        index_j = (column // 3)*3
        for add_i in range(3):
            for add_j in range(3):
                if self.val_index(index_i+add_i,index_j+add_j) != 0:
                    pos = 9-self.val_index(index_i+add_i,index_j+add_j)
                    back = ans & ((1 << (pos)) -1)
                    front = ans >> (pos+1)
                    ans = (front << (pos+1)) + back
        arr_ans = []
        for i in range(1,10):
            if ans & (1 << (9-i)):
                arr_ans.append(i)
        return arr_ans
    
    def solve_block(self, row, column):
        # recursion function
        # base case
        if row == 8 and column == 8:
            if self.val_index(8,8) != 0:
                self.show_board()
                print()
                self.solution = self.num_board
            else:
                self.change_block(8,8, self.possible_num(8,8)[0])
                self.show_board()
                print()
                self.solution = self.num_board
            return True
        if column == 8:
            next_block = (row+1, 0)
        else:
            next_block  = (row, column + 1)
        if self.val_index(row, column) != 0:
            return self.solve_block(next_block[0], next_block[1])
            
        else:
            if len(self.possible_num(row, column)) == 0:
                return False
            temp = self.num_board
            for num in self.possible_num(row, column):
                self.num_board = temp
                self.change_block(row, column, num)
                ans = self.solve_block(next_block[0], next_block[1])
                if ans == True:
                    return True
    
    def solve(self):
        print(self.solve_block(0,0))