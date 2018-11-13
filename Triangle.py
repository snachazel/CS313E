
#  File: Triangle.py

#  Description: A program to explore finding the greatest sum path in 4 different ways

#  Student's Name: Stephen Nachazel

#  Student's UT EID:sdn443

#  Course Name: CS 313E 

#  Unique Number:  51345

#  Date Created: 10/ 28 /18

#  Date Last Modified: 11/1/2018

from timeit import timeit

# returns the greatest path sum using exhaustive search
def brute_force (grid):
    
    #initialize the list to place all sums in
    sums = []
    brute_force_helper(grid, 0 , 0 , 0, sums)
    
    #return the list of sums
    return sums

def brute_force_helper(grid , row , index , sum, sums):
    
    #base case to append sum to list
    if row == len(grid):
        
        sums.append( sum)
        
    else:
        
     #add each element to prior sum to get all sums
     sum += grid[row][index]
     
     #return either the straight down element or the next element
     return brute_force_helper(grid , row + 1, index , sum, sums) or brute_force_helper(grid , row  + 1 , index + 1 , sum, sums)

# returns the greatest path sum using greedy approach
def greedy (grid):
    
  return greedy_helper(grid, 0 , 0)


def greedy_helper(grid ,index , sum):
    
    for i in range(len(grid) - 1):
        
        sum += grid[i][index]
       
        if grid[ i + 1][index] >= grid[ i + 1][index + 1]:
            
            index = index
        
        else:
            
            index += 1
            
    return sum
        
# returns the greatest path sum using divide and conquer (recursive) approach
def divide_conquer (grid):
    
  #initialize a palce to put each of the triangle sums
  sums = []
  divide_helper(grid , 0 , sums)
  
  #return the max of this smaller list of sums
  return max(sums)

def divide_helper(grid , sum , sums):
    
    #if only one row, return the element
    if len(grid) == 1:
        
        sums.append(sum + grid[0][0])
        
    else:
        #initialize the two triangles to divide the larger into
        left_path = []
        right_path = []
        
        #create the paths for each of the triangles
        for row in grid[1:]:
            left_path.append(row[1:])
            right_path.append(row[:-1])
            
        #add the element at the top of each of the triangles
        sum = sum + grid[0][0]
        
        #return each of the triangles
        return (divide_helper(left_path ,sum , sums) or divide_helper(right_path , sum , sums))
        
# returns the greatest path sum and the new grid using dynamic programming
def dynamic_prog(grid):
    
    return dyn_helper(grid , 0 ,0)
 
def dyn_helper (grid, row, index):
  
  if row == len(grid):
    #if nothing is there, return nothing
    return 0
  else:
    
    #calculate thhe two possible sums from the bottom up
    path1 = grid[row][index] + dyn_helper (grid, row + 1, index)
    path2 = grid[row][index] + dyn_helper (grid, row + 1, index + 1)
    
    #choose the maxima of the two sum options 
    return max(path1,path2)

# reads the file and returns a 2-D list that represents the triangle
def read_file ():
    
  in_file = open("triangle.txt" , "r")
  grid = []
  rows = in_file.readline()
  rows = int(rows)
  
  for line in range(rows):
      
      line = in_file.readline()
      line.strip()
      line = line.split()
      grid.append(line)
      
  for i in range(len(grid)):
      
      for j in range(len(grid[i])):
          
          grid[i][j] = int(grid[i][j])
          
  return grid
  

def main ():
  # read triangular grid from file
  grid = read_file()

  # output greatest path from exhaustive search
  sums  = brute_force(grid)
  brute_sum = max(sums)
  times = timeit ('brute_force({})'.format(grid), 'from __main__ import brute_force', number = 10)
  times = times / 10
  
  # print time taken using exhaustive search
  print("The greatest path sum using exhaustive search is " , brute_sum ,".")
  print("The time taken for exhaustive search is ", times, " seconds.")
  print()
  
  
  # output greatest path from greedy approach
  times = timeit ('greedy({})'.format(grid), 'from __main__ import greedy', number = 10)
  times = times / 10
  greedy_sum = greedy(grid)
  
  # print time taken using greedy approach
  print("The greatest path sum using greedy approach is " , greedy_sum,".")
  print("The time taken for greedy approach is ", times, " seconds.")
  print()
  
  
  # output greatest path from divide-and-conquer approach
  times = timeit ('divide_conquer({})'.format(grid), 'from __main__ import divide_conquer', number = 10)
  times = times / 10
  recursive_sum = divide_conquer(grid)
  
  # print time taken using divide-and-conquer approach
  print("The greatest path sum through recursive approach is " ,recursive_sum,".")
  print("The time taken for recursive search is ", times, " seconds.")
  print()
  
  
  # output greatest path from dynamic programming 
  times = timeit ('dynamic_prog({})'.format(grid), 'from __main__ import dynamic_prog', number = 10)
  times = times / 10
  dynamic_sum = dynamic_prog(grid)
  # print time taken using dynamic programming
  print("The greatest path sum using dynamic programming is " , dynamic_sum,".")
  print("The time taken for dynamic programming is ", times, " seconds.")

main()