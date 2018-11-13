# -*- coding: utf-8 -*-

# =============================================================================
# #  File: Work.py 
# 
# #  Description: This program finds the minimum number of lines of code to write in the first step to meet n
# 
# #  Student Name:  Stephen Nachazel
# 
# #  Student UT EID:sdn443  
# 
# #  Course Name: CS 313E
# 
# #  Unique Number: 51345
# 
# #  Date Created: 10 / 7 / 18
# 
# #  Date Last Modified: 10 / 8 /18 
# =============================================================================

def num_lines( n , k):
    
     #this initializes the lo and hi values for the modified binary search
     low = 1 
     hi = n 
     
     while low <= hi:
         
         mid = (low + hi) // 2 
         
         #if the values don't satisfy the algorithm, readjust the lo value and 
         #run another iteration
         if not valid( n , k , mid):
             low = mid + 1 
        
        
        #if the values do work, lower the hi value and keep the mid that works 
         elif valid( n , k ,  mid):
             hi = mid - 1 
             v = mid 
    
    #once lo is greater than hi return the mid, which is the minimum numbe of lines 
     return v
 
def valid( a , b , c ):
    
    #this initializes the exponent to raise the productivity factor 
    power = 1 
    lines_written = c
    
    
    #this conditional states that if the lines written are fewer than the necessary number
    #and the number of lines added is nonzero, keep increasing the power
    while (lines_written < a) and ((c // (b ** power )) != 0 ):
        
         lines_written += c // (b ** power )
         power += 1
    
    #returns a boolean in order to check if the mid, lo and hi values satisfy the conditions of the problem
    #such that lines written is the minimum possible value to meet a
    return (lines_written >= a)
   
  # do not remove this line above main()                        
if __name__ == '__main__':    
    def main():
        #opening and reading the file to determine number of cases
        infile = open("work.txt" , "r")
        cases = infile.readline()
        cases = int(cases)
        
        for i in range(cases):
            
            line = infile.readline()
            factors = line.split(" ")
            
            #assigning n and k from the file
            n = factors[0]
            k = factors[1]
            
            #converting the strings into integers
            n = int(n)
            k = int(k)
            
            #printing output 
            print( num_lines( n , k))
        infile.close()   
    main()
         
        