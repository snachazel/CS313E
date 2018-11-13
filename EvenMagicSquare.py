# -*- coding: utf-8 -*-

#  File: EvenMagicSquare.py

#  Description: Print all Magic squares of order 4 

#  Student Name: Stephen Nachazel 

#  Student UT EID:sdn443

#  Course Name: CS 313E

#  Unique Number: 51345

#  Date Created:10/19/18

#  Date Last Modified:10/22/18

#This function takes the permutation of integers and converts it into a 2D list to print
counter = 0
def convert(a):
    row1 = [a[0] , a[1] , a[2] , a[3]]
    row2 = [a[4] , a[5] , a[6] , a[7]]
    row3= [a[8] , a[9] , a[10] , a[11]]
    row4 = [a[12] , a[13] , a[14] , a[15]]

    a2 = [row1 , row2 , row3 , row4]
    return a2
#this recursive function takes a list and a starting index and generates all permutations 
def permute (a, lo , n):
    global counter
    if n == counter:
        return
    else:
      hi = len(a)
      if (lo == hi):
         #this is checking the final row sum
        if ( a[12] + a[13] + a[14] + a[15] )!= 34:
            return
        else:
          #if the square is a magic square, print out said square 
           if check_square(a):
              two = convert(a)
              print_square(two)
              counter  = counter  +  1
      else:
          #heck if the permutation of the first row adds to 34
          #if not return but if it does, continue permuting 
          if lo == 4:
              if (a[0] + a[1] + a[2] + a[3]) != 34:
                  return
              else:
                for i in range (lo, hi):
                    b= a[:]
                    b[lo], b[i] = b[i], b[lo]
                    permute (b, lo + 1 , n)
                    b[lo], b[i] = b[i], b[lo] 
         
        #heck if the permutation of the second row adds to 34
          #if not return but if it does, continue permuting 
          elif lo == 8:
              if (a[4] + a[5] + a[6] + a[7]) != 34:
                  return
              else:
                for i in range (lo, hi):
                    b= a[:]
                    b[lo], b[i] = b[i], b[lo]
                    permute (b, lo + 1 , n)
                    b[lo], b[i] = b[i], b[lo] 
          
          #heck if the permutation of the first row adds to 34
          #if not return but if it does, continue permuting 
          elif lo == 12:
              if (a[8] + a[9] + a[10] + a[11]) != 34:
                  return
              else:
                for i in range (lo, hi):
                    b= a[:]
                    b[lo], b[i] = b[i], b[lo]
                    permute (b, lo + 1 , n)
                    b[lo], b[i] = b[i], b[lo] 
         # if the idx is not divisible by 4 , continue permuting 
          else:
            for i in range (lo, hi):
              b= a[:]
              b[lo], b[i] = b[i], b[lo]
              permute (b, lo + 1 , n)
              b[lo], b[i] = b[i], b[lo]

#since this is always a 4x4, it is possible to hard code the values of what 
 #each row can be and set them as boolean flags          
def check_square(a):
    col1 = (a[0] + a[4] + a[8] + a[12] == 34)
    col2= (a[1] + a[5] + a[9] + a[13] == 34)
    col3 =(a[2] + a[6] + a[10] + a[14] == 34)
    col4 = (a[3] + a[7] + a[11] + a[15] == 34)
    cols = col1 and col2 and col3 and col4
    ld = (a[0] + a[5] + a[10] + a[15] == 34) 
    rd = (a[3] + a[6] + a[9] + a[12] == 34)
    ds = rd and ld
    return ds and cols


def print_square ( a ):
    #These values initalize the loop for printing the magic square
    n = len(a)
    row_print_idx = 0 % n
    col_print_idx = 0 % n
    spaces = len(str(n**2))
    #These loops print the magic square
    for elements in a:
        for elements in a[row_print_idx]:
                print( str(a[row_print_idx][col_print_idx]).rjust(spaces), end = ' ')
                col_print_idx = (col_print_idx + 1) % n
        print()        
        row_print_idx = (row_print_idx + 1) % n
    print()
def main():
    try:
        n = eval(input("Enter number of magic squares (1 - 10): "))
        print()
        while n < 1 or n > 10:
            n = eval(input("Enter number of magic squares (1 - 10): "))
        integers = []
        for i in range( 16):
            integers.append(int(i + 1))
        permute(integers , 0 , n)
    except SyntaxError:
         print("Incorrect input.")
    except NameError: 
         print("Incorrect Input.")

main()