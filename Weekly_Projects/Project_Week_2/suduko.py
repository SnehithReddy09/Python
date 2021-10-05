import numpy as np

class suduko_solver:
    board = np.array([ [3, 0, 6, 5, 0, 8, 4, 0, 0], 
         [5, 2, 0, 0, 0, 0, 0, 0, 0], 
         [0, 8, 7, 0, 0, 0, 0, 3, 1], 
         [0, 0, 3, 0, 1, 0, 0, 8, 0], 
         [9, 0, 0, 8, 6, 3, 0, 0, 5], 
         [0, 5, 0, 0, 9, 0, 6, 0, 0], 
         [1, 3, 0, 0, 0, 0, 2, 5, 0], 
         [0, 0, 0, 0, 0, 0, 0, 7, 4], 
         [0, 0, 5, 2, 0, 6, 3, 0, 0]])

    def row_checking(self,row,digit):
        for i in range(0,9):
            if self.board[row][i]==digit:
                return False 
        return True 

    def column_checking(self,column,digit):
        for i in range(0,9):
            if self.board[i][column]==digit:
                return False 
        return True 

    def square_checking(self,row,column,digit):
        a=(row//3)*3
        b=(column//3)*3
        for i in range(0,3):
            for j in range(0,3):
                if self.board[a+i][b+j]==digit:
                    return False 
        return True 

    def put_digit(self,row,column):
        for digit in range(1,10):
            if self.row_checking(row,digit) and self.column_checking(column,digit) and self.square_checking(row,column,digit):
                self.board[row][column]=digit 
                self.start_solving()
                self.board[row][column]=0
        return    

    def display(self):
        print(np.matrix(self.board))

    def start_solving(self):
        for i in range(0,9):
            for j in range(0,9):
                if self.board[i][j]==0:
                    self.put_digit(i,j)
                    return 
        self.display()



obj=suduko_solver()
obj.start_solving()

''' OUTPUT 

[[3 1 6 5 7 8 4 9 2]
 [5 2 9 1 3 4 7 6 8]
 [4 8 7 6 2 9 5 3 1]
 [2 6 3 4 1 5 9 8 7]
 [9 7 4 8 6 3 1 2 5]
 [8 5 1 7 9 2 6 4 3]
 [1 3 8 9 4 7 2 5 6]
 [6 9 2 3 5 1 8 7 4]
 [7 4 5 2 8 6 3 1 9]] '''