# -*- coding: utf-8 -*-
# =============================================================================
# File: MagicSquare.py
# 
# Description:Given an odd number greater than 1, this program generates an n dimensional magic square.
# 
# Student's Name: Stephen Nachazel
# 
# Student's UT EID: sdn443
#  
# Partner's Name:N/A
# 
# Partner's UT EID: N/A
# 
# Course Name: CS 313E 
# 
# Unique Number: 51345
# 
# Date Created: 9/4/2018
# 
# Date Last Modified: 9 / 7 / 2018
# =============================================================================
# Populate a 2-D list with numbers from 1 to n2
# This function must take as input an integer. You may assume that
# n >= 1 and n is odd. This function must return a 2-D list (a list of
# lists of integers) representing the square.
# Example 1: make_square(1) should return [[1]]
# Example 2: make_square(3) should return [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
def make_square (n):
    #This is the initial empty list
    magic_square= []
    #This loop generates the 2-D list for the magic square 
    for k in range(0, n):
        magic_square.append([])
    #This loop appends zeroes to the 2D list 
    for i in magic_square:
        for j in range(n):
            magic_square[j].append( 0 )
    #This initializes values to use for generating the Magic Square
    x = n - 1
    col_idx = (x // 2)
    row_idx = x 
    counter = 1 
    #This loop generates the non zero values for the n-dimensional magic square
    while counter <= n ** 2 :
        if magic_square[row_idx][col_idx] == 0:
            magic_square[row_idx][col_idx] = counter
            row_idx = (row_idx + 1 ) % n 
            col_idx = (col_idx + 1) % n 
            counter = counter + 1
        else:   
            row_idx = (row_idx - 2 ) % n
            col_idx = (col_idx - 1) % n 
            magic_square[row_idx][col_idx] = counter
            row_idx = (row_idx + 1 ) % n 
            col_idx = (col_idx + 1) % n 
            counter = counter + 1
    return magic_square
# Print the magic square in a neat format where the numbers
# are right justified
# This function must take as input a 2-D list of integers
# This function does not return any value
# Example: Calling print_square (make_square(3)) should print the output
# 4 9 2
# 3 5 7
# 8 1 6
def print_square ( magic_square ):
    #These values initalize the loop for printing the magic square
    n = len(magic_square)
    row_print_idx = 0 % n
    col_print_idx = 0 % n
    spaces = len(str(n**2))
    #These loops print the magic square
    for elements in magic_square:
        for elements in magic_square[row_print_idx]:
                print( str(magic_square[row_print_idx][col_print_idx]).rjust(spaces), end = ' ')
                col_print_idx = (col_print_idx + 1) % n
        print()        
        row_print_idx = (row_print_idx + 1) % n
# Check that the 2-D list generated is indeed a magic square
# This function must take as input a 2-D list, and return a boolean
# Example 1: check_square([[1, 2], [3, 4]]) should return False
# Example 2: check_square([[4, 9, 2], [3, 5, 7], [8, 1, 6]]) should return True
def check_square ( magic_square ):
    n = len(magic_square)
    canonicalSum = (n * (n**2 + 1)) // 2 
    magic = True
    sum_list = [] 
    row_sum_idx = 0 
    #This loop sums the rows
    for i in magic_square:
        row_sum = sum(magic_square[row_sum_idx])
        sum_list.append(row_sum)
        row_sum_idx += 1
    #These values initialize the loops for summing the diagonals
    left_diagonal_sum = 0 
    right_diagonal_sum = 0 
    ldri = 0
    ldci = 0 
    rdri = 0 
    rdci = 2 
    #This loop sums both diagonals
    for m in range(0, n):
        left_diagonal_sum += magic_square[ldri][ldci]
        right_diagonal_sum += magic_square[rdri][rdci]
        ldri += 1
        ldci += 1 
        rdri += 1
        rdci -= 1 
    sum_list.append(left_diagonal_sum)
    sum_list.append(right_diagonal_sum)
    #This loop sums the columns
    for v in range(0 , n ):
        col_sum = 0
        for u in range( 0 , n):
            col_sum += magic_square[v][u]
        sum_list.append(col_sum)    
    #This loop checks each of the sums against the canonical sum and returns false if
    #the values do not match       
    for element in sum_list:
        if element != canonicalSum:
            magic = False 
    return magic 
# This line above main is for grading purposes. It will not affect how
# your code will run while you develop and test it.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
    def main():
        #This is the dimension of the magical square based on user input
        n = eval(input("Please enter an odd number greater than 1: "))
        canonicalSum = (n * (n**2 + 1)) // 2  
        #These are conditions to test if the inout is valid
        size = n > 1
        odd = (n % 2 == 1 )
        valid = size and odd 
        #This loop prompts a user for valid input if their first input is incorrect
        while not(valid):
            n = eval(input("Please enter an odd number greater than 1  : "))
            canonicalSum = (n * (n**2 + 1)) // 2 
            size = n > 1
            odd = (n % 2 == 1 )
            valid = size and odd 
        magic_square = make_square ( n ) 
        #These conditionals check if a magic square was generated
        #and output the square and its canonical sum if magic
        if check_square ( magic_square ):
             print()
             print("Here is a", n , "x", n , "magic square:") 
             print()
             print_square ( magic_square )
             print()
             print("This is a Magic Square and the canonical sum is" , canonicalSum)
        else:
             print()
             print("Here is a", n , "x", n , "magic square:") 
             print()
             print_square ( magic_square )
             print()
             print("This is not a magic Square.")
    main()
    
