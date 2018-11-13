#  File: TestLinkedList.py

#  Description: Finish the Linked List Class 

#  Student's Name: Stephen Nachazel

#  Student's UT EID: sdn443

#  Course Name: CS313e

#  Unique Number: 51345

#  Date Created: 11/3/18

#  Date Last Modified: 11/5/18

class Link (object):
	def __init__(self, data, next = None):
        
		self.data = data
		self.next = next

	def __str__(self):
		return str(self.data)

class LinkedList (object):
    
	# initialize
	def __init__(self):
		self.first = None
	
	# String representation of data 10 items to a line, 2 spaces between data
	def __str__ (self):
		line = ""
		current = self.first

		elements = 0

		while (current != None):

			line += str(current.data) + "  "
			current = current.next
			# increment counter
			elements += 1

			# check if 10 elements
			if (elements % 10 == 0):
				# start a new line items
				line += "\n"


		# return final output
		return line

	# get number of links 
	def get_num_links (self):
		current = self.first
		if (current == None):
			return 0
		count = 1

		while (current.next != None):
			current = current.next
			# increment count
			count = count + 1
		return count
	
	# insert data at the beginning of the list
	def insert_first (self, data):
		new_link = Link(data)
		
		new_link.next = self.first
		self.first = new_link

	# insert data at the end of a list
	def insert_last (self, data):
		new_link = Link(data)
		
		current = self.first
		
		if (current == None):
			self.first = new_link
			return

		while (current.next != None):
			current = current.next
		current.next = new_link


	# insert_ data in an ordered list in ascending order
	def insert_in_order (self, data):
		new_link = Link(data)

		current = self.first

		previous = self.first

		if (current == None) or (current.data >= data):
			new_link.next = self.first
			self.first = new_link
			return

		while (current.next != None):
			if (current.data <= data):
				previous = current
				current = current.next
			else:
				new_link.next = previous.next
				previous.next = new_link
				return

		if (current.data <= data):
			current.next = new_link
		else:
			new_link.next = previous.next
			previous.next = new_link
		return


	# Search in an unordered list, return None if not found
	def find_unordered (self, data):
		current = self.first

		if (current == None):
			return None

		while(current != None):
			if (current.data == data):
				return current
			else:
				current = current.next

		return current

	# Search in an ordered list, return None if not found
	def find_ordered (self, data):
		current = self.first

		if (current == None):
			return None 

		while (current != None):
			if (current.data == data):
				return current
			else:
				current = current.next

		return current

	# delete and return Link from an unordered list or None if not found
	def delete_link (self, data):
		current = self.first
		previous = self.first

		if (current == None):
			return None

		while(current.data != data):
			if (current.next == None):
				return None
			else:
				previous = current
				current = current.next

			if (current == self.first):
				self.first = self.first.next
			else:
				previous.next = current.next

		return current


	# Copy the contents of a list and return new list
	def copy_list (self):
		copied_list = LinkedList()
		current = self.first
		
		while (current != None):
			copied_list.insert_last(current.data)
			current = current.next

		return copied_list

	# Reverse the contents of a list and return new list
	def reverse_list (self):
		reverse_list = LinkedList()
		current = self.first

		# start inserting data from beginning
		while (current != None):
			reverse_list.insert_first(current.data)
			current = current.next

		return reverse_list


	# Sort the contents of a list in ascending order and return new list
	def sort_list (self): 
		sorted_list = LinkedList()
		current = self.first

		while (current != None):
			# insert in ascending order
			sorted_list.insert_in_order(current.data)
			if (current.next != None):
				current = current.next
			else:
                
				break 

		return sorted_list

	# Return True if a list is sorted in ascending order or False otherwise
	def is_sorted (self):
		current = self.first

		while (current.next != None):
			if (current.data <= current.next.data):
				current = current.next
			else:
				return False

		return True

	# Return True if a list is empty or False otherwise
	def is_empty (self): 
		if (self.first == None):
			return True
		else:
			return False

	# Merge two sorted lists and return new list in ascending order
	def merge_list (self, other):
		# check if lists are empty
		if (self.is_empty() == True):
			return other
		elif (other.is_empty() == True):
			return self

		merge_list = LinkedList()

		sstart = self.first
		ostart = other.first
		#while both lists have not yet reached the end
		while ((sstart != None) and (ostart != None)):
			if (sstart.data < ostart.data):
				merge_list.insert_last(sstart.data)
				sstart = sstart.next
			else: 
				merge_list.insert_last(ostart.data)
				ostart = ostart.next

		# sort list self
		while (ostart != None):
				merge_list.insert_last(ostart.data)				
				ostart = ostart.next				

		while (sstart != None):
				merge_list.insert_last(sstart.data)
				sstart = sstart.next

		return merge_list

	# Test if two lists are equal, item by item and return True
	def is_equal (self, other):
		sstart = self.first
		ostart= other.first

		if self.get_num_links() != other.get_num_links():
			return False

		elif self.is_empty() and other.is_empty():
			return True

		else:
			for i in range(self.get_num_links()):
				if (sstart.data != ostart.data):
					return False
				else:
					sstart = sstart.next
					ostart = ostart.next					

			return True
			

	# Return a new list, keeping only the first occurence of an element
	# and removing all duplicates. Do not change the order of the elements.
	def remove_duplicates (self):
		no_duplicates_list = LinkedList()
		current = self.first

		no_duplicate = []

		while (current != None):
			# check if value exists
			if (current.data in no_duplicate):
				pass
			else:
				no_duplicate.append(current.data)
				# then insert_ that value to the 'old' list
				no_duplicates_list.insert_last(current.data)
				

			
			current = current.next

		return no_duplicates_list


def main():

    testList = [ 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 11 , 12  ,13 , 14]
    unordered_test_list = [ 1 , 3 ,4 , 6 ,7 ,8 ,10 , 9 , 2 ,11 , 14 , 13 ,12 ,0]
    duplicates = [ 1 , 1 , 3 ,3 , 2 , 2 ,2 ]
    mtest1 = [ 1 , 3 , 5 , 7 , 9 , 11]
    mtest2 = [ 2 , 4 , 6 , 8 , 10 , 12]
    	# Test method insert_first()
    print("Test method insert_first")
    test = LinkedList()
    utest = LinkedList()
    dtest = LinkedList()
    empty = LinkedList()
    mltest1 = LinkedList()
    mltest2 = LinkedList()
    otest = LinkedList()
    for item in testList:
    	test.insert_first(item)
    for item in testList:
    	otest.insert_in_order(item)
    for item in unordered_test_list:
        utest.insert_first(item)
    for item in duplicates:
        dtest.insert_first(item)
    for item in mtest1:
        mltest1.insert_in_order(item)
    for item in mtest2:
        mltest2.insert_in_order(item)    
    print(test)
    print()
    
    
    # Test method insert_last()
    print("Test method insert_last")
    	# create new LinkedList object
    test.insert_last(0)
    print(test)
    print()
    
    
    # Test method insert_in_order()
    print("Test method insert_in_order")
    
    # create new LinkedList object
    test.insert_in_order(1)
    print(test)
    print()
    
    
    # Test method get_num_links()
    print("Test method get_num_links")
    	
    print(test.get_num_links())
    print()
    
    
    # Test method find_unordered() 
    # Consider two cases - item is there, item is not there 
           
    print("Test method find_unordered")
    print(utest.find_unordered(13))
    print(utest.find_unordered(23))
    print()
    	
    
    
    # Test method find_ordered()
    # Consider two cases - item is there, item is not there 
    # item not there
    print("Test method find_ordered")
    print(otest.find_ordered(9) )
    # item there
    print(otest.find_ordered(17))
    print()
    
    print("Test method delete_link")
    # Consider two cases - item is there, item is not there 
    print(test.delete_link(1))
    print(test.delete_link(19))	
    print()
    
    # Test method copy_list()
    print("Test method copy_list")
    print(test)
    print(test.copy_list())
    print()
    
    # Test method reverse_list()
    print("Test method reverse_list")
    print(test)
    print(test.reverse_list())
    print()
    
    	
    
    # Test method sort_list()
    print("Test method sort_list")
    print(utest)
    print(utest.sort_list())
    print()
    
    # Test method is_sorted()
    print("Test method is_sorted")
    # Consider two cases - list is sorted, list is not sorted
    print(utest)
    print(utest.is_sorted())
    print()
    
    # Test method is_empty()
    print("Test method is_empty")
    print(test)
    print(test.is_empty())
    print(empty)
    print(empty.is_empty())
    print()
    	
    
    # Test method merge_list()
    print("Test method merge_list")
    print(mltest1.merge_list(mltest2))
    print()
    
    
    print("Test method is_equal")
    # Consider two cases - lists are equal, lists are not equal
    print(test.is_equal(test))
    print(test.is_equal(dtest))
    print()
    
    # Test remove_duplicates()
    print("Test remove_duplicates")
    print(dtest.remove_duplicates())
    print()
    
main()

if __name__ == "__main__":
  main()