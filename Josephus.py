#  File: Josephus.py

#  Description: Using Circular Linked Lists, present a solution to the josephus problem

#  Student Name: Stephen Nachazel

#  Student UT EID: sdn443

#  Course Name: CS 313E

#  Unique Number: 51345

#  Date Created: 11/ 5 / 2018 

#  Date Last Modified: 11 / 9 / 2018

class Link(object):
    
    def __init__(self , data , next = None):
        
        #initialize the data and pointer
        self.data = data
        self.next = next


class CircularList(object):
    
  # Constructor
  def __init__ ( self ): 
      
      self.first = None

  # Insert an element (value) in the list
  def insert ( self, data):
      
      #create a new link
      new_link = Link(data)
      
      #if the first link is null, insert new link here
      if self.first == None:
          
          self.first = new_link
          self.first.next = self.first
          return
      
      else:
          
          current = self.first
          
          #find the end of the list
          while (current.next != self.first):
              current = current.next
          
          #insert the new link at the end of the list
          current.next = new_link
          current = current.next
          current.next = self.first
          return 
          

  # Find the link with the given data (value)
  def find ( self, data ):
      current = self.first
      if current == None:
          return None
      else:
          #if there is only one element, check if it is the desired data
          if current.next == self.first :
              #if it is, return it
              if current.data == data:
                  return current
              else:
                  return None
              
          #so long as the list is not at the end
          while current.next != self.first:
              
              #check if the current link is the necessary data, if not advance
              if current.data == data:
                  return current
              else:
                  current = current.next
                  
          #if the last link is the required data, return it else return none        
          if current.data == data:
              return current
          else:
              return None

  # Delete a link with a given data (value)
  def delete ( self, data ):
      #initialize the links on either side of the deleted link
      current = self.first
      previous = self.first
      
      #advance to the end of the list
      while previous.next != self.first:
          previous = previous.next
          
      #if the current element is None, return none
      if current == None:
          return None
      
      else:
          
          #if the current data is wha you want and is first, return it 
          if current.next == self.first:
              if current.data == data:
                  return current
              
         #while data doesn't match
          while current.data != data:
              
              #if you're at the end of the list, return none
              if current.next == self.first:
                  
                  return None
              
              else: 
                  #advance through the list
                  previous = current
                  current = current.next
               
          if current == self.first:
              self.first = self.first.next
          previous.next = current.next
          
       #return the data you're looking for        
      return current.data

  # Delete the nth link starting from the Link start 
  # Return the next link from the deleted Link
  def delete_after ( self, start, n ):
      
      current = self.find(start)
      dead = ""
      
      while start != 1:
          current = current.next
          start -= 1 
      
      #while there is more than one soldier left
      while current.next != current:
           #get to the last soldier
           for i in range( n  - 1 ):
              current = current.next
              
           #get the last soldier's data
           soldier = current.data
           
           #delete the last soldier and add him to list 
           dead_soldier = self.delete(soldier)
           dead += str(dead_soldier) + "\n"
           current = current.next
           
      #appending the last surviving soldier to the list
      last_soldier = dead + str(current.data)
      print(last_soldier)
      
          
        
  
  # Return a string representation of a Circular List
  def __str__ ( self ):
      current = self.first
      if current == None:
          return
      
      line = str(current.data) + "\n"
      
      while current.next != self.first:
          
          line += str(current.next.data) + "\n"
          current = current.next
          
      return line
      

def main():
 #open the file
 in_file = open("josephus.txt" , "r" )
 
 #read in how big the group is
 num_soldiers = in_file.readline()
 num_soldiers = int(num_soldiers)
 
 #read in where the circle starts
 start_soldier = in_file.readline()
 start_soldier = int(start_soldier)
 
 #read in the step size
 increment = in_file.readline()
 increment = int(increment)
 
 #initialize the list
 battalion = CircularList()
 
 #fill the list with soldiers and their names
 for i in range( 1 , num_soldiers + 1):
     battalion.insert(i)
     
 #if list has elements, delete in the specified order
 if battalion.first != None:
      battalion.delete_after(start_soldier , increment)
      
 #if list is empty, print the list
 else:
     print ( battalion)
 #close file
 in_file.close() 
 
main()

