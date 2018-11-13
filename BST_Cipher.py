#  File: BST_Cipher.py

#  Description: A encryption method using Binary Search Trees 

#  Student Name: Stephen Nachazel

#  Student UT EID: sdn443

#  Course Name: CS 313E

#  Unique Number: 51345

#  Date Created: 11/ 10 /18

#  Date Last Modified: 11/ 12 /18

class Node(object ):
    
    def __init__(self , data):
        
        #each node has data, a left child and a right child
        self.data  = data 
        self.lchild = None
        self.rchild = None
        
    def __str__(self):
        return str(self.data)
        

class Tree (object):
    
  # the init() function creates the binary search tree with the
  # encryption string. If the encryption string contains any
  # character other than the characters 'a' through 'z' or the
  # space character drop that character.
  def __init__ (self, encrypt_str):
      
      
      self.root = None
      
      #create a set in order to ensure no duplicate characters 
      chars = set()
      
      #create a tree from the set
      for char in encrypt_str:
          chars.add(char)
      for char in chars:
          self.insert(char)
      
      

  # the insert() function adds a node containing a character in
  # the binary search tree. If the character already exists, it
  # does not add that character. There are no duplicate characters
  # in the binary search tree.
  def insert (self, ch):
      
      #create a new node
      new_node = Node(ch)
      
      #if the tree is empty, this is the first node
      if self.root == None:
          self.root = new_node
          
      #initialize placeholder values  
      current = self.root
      parent = self.root
      
      # find the end of the appropriate sub tree
      while (current != None):
          
          parent = current
          if ch < current.data:
              current = current.lchild
          else:
              current = current.rchild
              
      # if the character is already in the tree,do nothing        
      if ch == parent.data:
         return
     
      elif ch < parent.data:
          parent.lchild = new_node
          
      else:
          parent.rchild = new_node
      
  # the search() function will search for a character in the binary
  # search tree and return a string containing a series of lefts
  # (<) and rights (>) needed to reach that character. It will
  # return a blank string if the character does not exist in the tree.
  # It will return * if the character is the root of the tree.
  def search (self, ch):
      
      #by convention , the root is a * in the encoded string
      if self.root == ch:
          
          return "*"
      
      else:
          
          element = ""
          current = self.root
          
          #add the correct characters for a path in the tree
          while (current != None) and (current.data != ch):
              
              if ch < current.data:
                  
                  element = element + "<"
                  current = current.lchild
                  
              else:
                  
                  element = element + ">"
                  current = current.rchild
          
          #if the character is not in the tree, return none  
          if current == None:
              return ""
          
            #if the character is in the tree, return the path
          else:
              return element
                  
      
             

  # the traverse() function will take string composed of a series of
  # lefts (<) and rights (>) and return the corresponding 
  # character in the binary search tree. It will return an empty string
  # if the input parameter does not lead to a valid character in the tree.
  def traverse (self, st):
      
      current = self.root
      
      if st == "*":
          
          return current.data
      
      for char in st:
          
          if char =="<":
              current = current.lchild
              
          if char == ">":
              current = current.rchild
              
      return current.data

  # the encrypt() function will take a string as input parameter, convert
  # it to lower case, and return the encrypted string. It will ignore
  # all digits, punctuation marks, and special characters.
  def encrypt (self, st):
      
      st = st.lower()
      st = st.strip()
      
      encrypted_st = ""  
      
      for i in range( len(st)):
          
          if st[i].isalpha() or st[i].isspace():
              element = self.search(st[i])
              encrypted_st = encrypted_st + str(element) + "!"
              
      return encrypted_st[:-1]
       

  # the decrypt() function will take a string as input parameter, and
  # return the decrypted string.
  def decrypt (self, st):
      #initialize a blank string to print out
      decrypted_st = ""
      
      #break the encoded string into its elements
      st_list = st.split("!")
      
      #decode the string
      for element in st_list:
          decrypted_st = decrypted_st + self.traverse(element)
          
       #return the plain text string      
      return decrypted_st
      
def main():
 
        key = "the quick brown fox jumps over the lazy dog"
        bst_tree = Tree(key)
        print("Enter encryption key: the quick brown fox jumps over the lazy dog")
        print()
        
        in_phrase = input("Enter phrase to be encrypted: ")
        encode = bst_tree.encrypt(in_phrase)
        print("Encrpyted phrase: " + str(encode))
        
        print()
        
        out_phrase = input("Enter phrase to be decrypted: ")
        decode = bst_tree.decrypt(out_phrase)
        print("Decoded phrase: " + str(decode))

    
    
main()
