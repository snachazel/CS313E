#  File: Queens.py

#  Description:

#  Student Name:Stephen Nachazel

#  Student UT EID:sdn443

#  Course Name: CS 313E

#  Unique Number: 51345

#  Date Created: 10/25/18

#  Date Last Modified:10/29/18  

#global counter variable to count the number of possible solutions for n queens
counter = 0
#initialize the class of Queens
class Queens (object):
  # initialize the board
  def __init__ (self, n = 8):
    self.board = []
    self.n = n
    for i in range (self.n):
      row = []
      for j in range (self.n):
        row.append ('*')
      self.board.append (row)

  # print the board
  def print_board (self):
    for i in range (self.n):
      for j in range (self.n):
        print (self.board[i][j], end = ' ')
      print ()
    print() 

  # check if no queen captures another
  def is_valid (self, row, col):
    for i in range (self.n):
      if (self.board[row][i] == 'Q' or self.board[i][col] == 'Q'):
        return False
    for i in range (self.n):
      for j in range (self.n):
        row_diff = abs (row - i)
        col_diff = abs (col - j)
        if (row_diff == col_diff) and (self.board[i][j] == 'Q'):
          return False
    return True

  # do a recursive backtracking solution
  def recursive_solve (self, col):
    global counter
    if (col == self.n):
        #this uses the helper function to see how many queens are present 
        num = self.count_Queen()
        if num == self.n:
            
          self.print_board()
          counter += 1 
          return True
    else:
      solvable = False 
      for i in range (self.n):
        if (self.is_valid(i, col)):
          self.board[i][col] = 'Q'
          solvable = self.recursive_solve(col + 1) or solvable 
          self.board[i][col] = '*'
      return 

  # if the problem has a solution print the board
  def solve (self):
    for i in range (self.n):
      self.recursive_solve(i)
 
  #this counts the numer of queens present in the solution and returns a sum    
  def count_Queen(self):
    qsum = 0
    for i in range(self.n):
        qsum +=  self.board[i].count('Q')
    return qsum
    
    
def main():
  try:
      
      # create a regular chess board
      n = eval(input("Enter size of board: "))
      print()
      while n <= 0 or n > 8:
          n = eval(input("Enter size of board: "))
          print()
      
      game = Queens (n)

      # place the queens on the board
      game.solve()
      
      print("There are " , counter ,"solutions for a ", str(n) , "x" , str(n ), "board.")
  
    #exception handling for user input
  except ValueError:
      print("Invalid Input.")
      
  except SyntaxError:
      print("invalid Input.")
  except TypeError:
      print("Invalid end.")
main()
