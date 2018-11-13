# -*- coding: utf-8 -*-

#  File: Boxes.py

#  Description: A program that recursively determines the subsets of boxes that can fit inside another

#  Student Name: Stephen Nachazel

#  Student UT EID: sdn443

#  Course Name: CS 313E

#  Unique Number: 51345

#  Date Created: 10/15/18

#  Date Last Modified: 10/17/18

def does_fit(a , b):
    #check if the smaller box is strictly smaller than the larger one
    #return a boolean
    return (a[0] < b[0]) and (a[1] < b[1]) and (a[2] < b[2])


def sub_sets( a  , b , c , idx ):
    
    end = len(a)
    fits = True 
    #base case is if function is at end of the list
    if idx == end:
        #check if all boxes in subset fit
        #if not, set flag to false
        for i in range(len(b) - 1 ):
            if not does_fit(b[i] , b[i+1]):
                fits = False
        
        #if all boxes fit, append subset to nested set
        if fits:
         c.append(b)
        return
    
    else:
        
        #construct subsets by adding or not adding box
        d = b[:]
        b.append(a[idx])
        sub_sets( a  , d , c , idx + 1 )
        sub_sets( a  , b , c , idx + 1 )

def main():
    #this segment of code opens the file and determines the numbe rof boxes
    in_file = open("boxes.txt" , "r")
    cases = in_file.readline()
    cases.strip()
    cases = int(cases)
    
    #if there is a negative number of boxes, exit the function
    if cases <= 0:
        print("This is not a valid number of cases")
        return
   
    #this segment of code initializes three empty lists 
    all_subsets = []
    all_boxes = []
    nested_boxes = []
    
    #this loop reads in all of the boxes and their dimensions in a usuable format
    for line in range(cases):
        
        case = in_file.readline()
        case.strip()
        case = case.split()
        
        #this segment changes each value from a character to an integer 
        for i in range(len(case)):
            case[i] = int(case[i])
        
        case.sort()
        all_boxes.append(case)
   
    #this sorts the boxes for easier iteration
    all_boxes.sort()
    
    #close the file
    in_file.close()
    
    #call the recursive function o create all subsets
    sub_sets(all_boxes , nested_boxes , all_subsets, 0)
    
    #initialize the max size of nested boxes
    max_size = 2
    
    #determine what the largest number of nested boxes can be 
    for element in all_subsets:
        if len(element) > max_size:
            max_size = len(element) 

    
    #collect all of the subsets of the largest dimension into a list
    biggest_subsets = []
    for element in all_subsets:
        if len(element) == max_size:
            biggest_subsets.append(element)
    
    #if there are no qualifying subsets, print such
    if len(biggest_subsets) == 0:
        print("No nesting boxes.")
    
    
    else:
        #print the largest subsets in the specified format
        print("Largest Subset of Nesting Boxes")
        biggest_subsets.sort()
        for element in biggest_subsets:
            for i in range(len(element)):
                print(element[i])
            print()
   
       
main()
        