# -*- coding: utf-8 -*-
# =============================================================================
# """
# #  File: PhoneBook.py
# 
# #  Description: An interactive program that allows the user to search and update a phone book
# 
# #  Student Name: Stephen Nachazel
# 
# #  Student UT EID: sdn443
# 
# #  Course Name: CS 313E
# 
# #  Unique Number:51345
# 
# #  Date Created: 9 / 17 / 2018
# 
# #  Date Last Modified: 9 / 21/ 2018
# =====================================3========================================
class ContactInfo (object):
  # constructor
  def __init__ (self, street, city, state, zip, country, phone, email):
      self.street = str(street)
      self.city = str(city)
      self.state = str(state)
      self.zip = str(zip) 
      self.country = str(country )
      self.phone = str(phone)
      self.email = str(email)
  # string representation of Contact Info
  def __str__ (self):
      print("Street: " + self.street + "\n")
      print ("City: " + self.city + "\n")
      print("State: " + self.state + "\n")
      print("Zip: " + self.zip + "\n")
      print("Country: " + self.country + "\n")
      print("Phone: " + self.phone + "\n")
      print("Email: " + self.email + "\n")
      
# Define global dictionary to hold all the contact information
phone_book = {}

# This function adds the contact information of a new person in the
# dictionary
def add_person():
    
  # Prompt the user to enter the name of the new person
  name = str(input("Please enter the name you're looking for: "))
  if name == "":
      pass
  # Check if name exists in phone book. If it does print a message
  # to that effect and return
  elif phone_book.get(name):
      print( name, "is already in the phonebook.")
      print()
      
  else:
      # Prompt the user to enter the required contact information
      street = str(input("Enter street: "))
      city = str(input("Enter city: "))
      state = str(input("Enter state: "))
      zip = str(input("Enter zip: "))
      country = str(input("Enter country: "))
      phone = str(input("Enter phone: "))
      email = str(input("Enter email: "))
      # Create the ContactInfo object
      contactObj = ContactInfo (street, city, state, zip, country, phone, email)
    
      # Add the name and the contact information to the phone dictionary
      phone_book[name] = contactObj
      # Print message that the information was added successfully
      print("The phone book was updated with information for " + name)
      print()
      
# This function deletes an existing person from the phone dictionary
def delete_person():
    
  # Prompt the user to enter the name of the person
  name = str(input("Please enter the name you're looking for: "))
  
  # If the name exists in phone book delete it.
  # Print message as to the action.
  
  #this conditional handles if the name does not exist at all in the phone ook
  if phone_book.get(name) == None:
      print( name, "does not exist in the phone book.")
      print()
      
  else:
       del phone_book[name]
       print( name , "has been deleted from the phonebook.")
       print()

# This function updates the information of an existing person 
def update_person():
    
  # Prompt the user to enter the name of the person
  name = str(input("Please enter the name you're looking for: "))
  
  # Check if name exists in phone book. If it does prompt
  # the user to enter the required information.
  if name in phone_book:
      #if the entered str is blank then the dorrespondin piece
      #of contact info is left unchanged
      street = str(input("Enter street: "))
      if street == "":
          pass
      else:
          phone_book[name].street = street
          
      city = str(input("Enter city: "))
      if city == "":
          pass
      else:
          phone_book[name].city = city
          
      state = str(input("Enter state: "))
      if state == "":
          pass
      else:
          phone_book[name].state = state
          
      zip = str(input("Enter zip: "))
      if zip == "":
          pass
      else:
          phone_book[name].zip = zip
          
      country = str(input("Enter country: "))
      if country == "":
          pass
      else:
          phone_book[name].country = country
          
      phone = str(input("Enter phone: "))
      if phone == "":
          pass
      else:
          phone_book[name].phone = phone
          
      email = str(input("Enter email: "))
      if email == "":
          pass
      else:
          phone_book[name].email = email
    
      print(name, "has been updated.")
      print()
      
  else:
     print(name, "is not in the phonebook.")
     print()
  # Write a message as to the action

# This function prints the contact information of an existing person
def search_person():
    
  # Prompt the user to enter the name of the person
  name = str(input("Please enter the name you're looking for: "))
  
  # Check if name exists in phone book. If it does print the
  # information in a neat format. 
  if name in phone_book:
      phone_book[name].__str__()
      
  # If the name does not exist print a message to that effect.
  else:
      print(name, "is not in the phone book.")
      
# This function open the file for writing and writes out the contents
# of the dictionary.
def save_quit():
    
  # Open file for writing
  open_file = open("./phone.txt" , "w")
  
  # Iterate through the dictionary and write out the items in the file
  for name in phone_book:
      open_file.write(str(name  + "\n"))
      open_file.write(str(phone_book[name].street  + "\n"))
      open_file.write(str(phone_book[name].city  + "\n"))
      open_file.write(str(phone_book[name].state  + "\n"))
      open_file.write(str(phone_book[name].zip  + "\n"))
      open_file.write(str(phone_book[name].country  + "\n"))
      open_file.write(str(phone_book[name].phone  + "\n"))
      open_file.write(str(phone_book[name].email + "\n"))
      open_file.write(str("\n"))
      
  # Close file
  open_file.close()
  # Print  message
  print("The phone book has been saved.")
  
# This function prints the menu, prompts the user for his/her selection
# and returns it.
def menu():
    
    #This loop asks the user for input based on the menu and returns the input
    #If the input is incorrect, the function asks for valid input until valid input
    #is entered 
    valid = False 
    while not valid:
        try:
            print()
            print("1. Add a Person")
            print()
            print("2. Delete a Person")
            print()
            print("3. Search for a Person")
            print()
            print("4. Update Information on a Person")
            print()
            print("5. Quit")
            print()
            option = eval(input("Enter your option: "))
            while option < 1 or option > 5:
                option = eval(input("Enter your option: "))
            return(option)
            valid = True
        except:
            not_acceptable = True 
            while not_acceptable:
                option = str(input("Enter your option: "))
                if option.isdigit() and int(option) < 6 and int(option) > 0:
                    return int(option)
                    not_acceptable = False 
                    break
                    
# This function opens the file for reading, reads the contact information
# for each person and adds it to the dictionary.
def create_phone_book():
    
  # Open file for reading
  in_file = open ("./phone.txt", "r")

  # Read first line (name)
  line = in_file.readline()
  line = line.strip()

  # Loop through the entries for each person
  while (line != ""):
    name = line
    # Read street
    street = in_file.readline().strip()
    # Read city
    city = in_file.readline().strip()
    # Read state
    state = in_file.readline().strip()
    # Read zip
    zip = in_file.readline().strip()
    # Read country
    country = in_file.readline().strip()
    # Read phone number
    phone = in_file.readline().strip()
    # Read e-mail address
    email = in_file.readline().strip()
    # Read blank line
    blank = in_file.readline().strip()
    # Read first line of the next block of data
    line = in_file.readline()
    line = line.strip()

    # Create ContactInfo object
    contactObj = ContactInfo( street , city , state, zip , country , phone , email)
    # Add to phone dictionary
    phone_book[name] = contactObj
  # Close file
  in_file.close()
  
def main():
    
  # Read file and create phone book dictionary
  create_phone_book()

  # Print logo
  print ("Phone Book")
  
  # Print menu and get selection
  selection = menu()
  # Process request, print menu and prompt again and again
  # until the user types 5 to quit.
  valid = True 
  while valid:
      if selection == 1:
          add_person()
          selection = menu()
      elif selection == 2:
          delete_person()
          selection = menu()
      elif selection == 3:
          search_person()
          selection = menu()
      elif selection == 4:
          update_person()
          selection = menu()
      elif selection == 5:
           save_quit()
           break 
      # Save and quit
      
  # Goodbye message
  print()
  print ("Thank you for using the Phone Book.\n")
  
main()