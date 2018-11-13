# -*- coding: utf-8 -*-
# =============================================================================
# #  File: BabyNames.py 
# 
# #  Description:  This is an interactive piece of software that allows users to look at data referring to the list of baby names in the US
# 
# #  Student Name:  Stephen Nachazel
# 
# #  Student UT EID:  sdn443
# 
# #  Course Name: CS 313E
# 
# #  Unique Number: 51345
# 
# #  Date Created:9/10/2018
# 
# #  Date Last Modified:9/14/2018
# =============================================================================

#This function creates the dictionary to analyze given the user input
#If the dictionary cannot be found, it outputs an error message 
def create_names():
    try:
        in_file = open("./names.txt" , "r")
        lines = in_file.readlines()
        names ={}
        for line in lines:
            name , dec1 , dec2 ,dec3 , dec4 , dec5 , dec6 , dec7 , dec8 , dec9 , dec10, dec11 = line.split(' ')
            name = name.lower()
            decades = [dec1 , dec2 ,dec3 , dec4 , dec5 , dec6 , dec7 , dec8 , dec9 , dec10, dec11]
            for i in range(len(decades)):
                decades[i] = int(decades[i])
            names[name] = decades
        return(names)
    except:
        print("The requested file cannot be found.")
    finally:
        in_file.close()

#This function is used to find the decade in which a certain name was ranked the highest  on the list    
def mostcommon(name , names):
    namesmc = names
    for x in namesmc:
        for i in range(len(namesmc[x])):
            if namesmc[x][i] == 0:
                namesmc[x][i] = 1001
    rankings = namesmc.get(name)
    common_idx = rankings.index(min(rankings))
    years = [ 1900 , 1910 , 1920 , 1930 , 1940 , 1950 , 1960 , 1970 , 1980 , 1990 , 2000]
    most = years[common_idx]
    return(most)
#This function is used by option 1
#Given a certain name, this function checks if such a name is in the list
def present(names , name):
    if name in names:
        return(True)
    else:
        return False 
    
#This corresponds to option 2 in the menu 
#This function takes the given name and outputs the ranks of the name for all decades
def one_name(names , name):
     if name in names:
         ranks = names[name]
         years = [ 1900 , 1910 , 1920 , 1930 , 1940 , 1950 , 1960 , 1970 , 1980 , 1990 , 2000]
         print()
         print(name.capitalize() , ":" , names[name])
         for i  in range(len(years)):
             print(years[i], ":" , ranks[i])
     else:
        print("There is no data for" , name)

#This corresponds to option 3 
#This function asks for a specific decade and prints out all names on the list in that decade
#ordered by their rank
def ordered_decade(names):
    try:
        decadeChoice = eval(input("Please enter a decade: "))
        years = [ 1900 , 1910 , 1920 , 1930 , 1940 , 1950 , 1960 , 1970 , 1980 , 1990 , 2000]
        decade_idx = years.index(decadeChoice)
        decadePresent = {}
        for name in names:
            if names[name][decade_idx] != 0:
                decadePresent[name] = names[name][decade_idx]
        decadePresent = sorted(decadePresent.items() , key = lambda x:x[1])
        decadePresent = dict(decadePresent)
        print("The names are in order of rank:")
        for name in decadePresent: 
            print(name.capitalize() , ': ' , decadePresent[name])
        print()
    except ValueError:
        print("You have entered an incorrect input.")
        print()
    except NameError:
        print("You have entered an incorrect character.")
        print()
 # This function checks if  a name is present in every decade on the list 
#This is a helper function used by otions 4 , 5 ,6  
def always(names):
    always = []
    for name in names:
        if names[name].count(0) == 0:
            always.append(name)
        else:
            pass               
    return(always)

#This function corresponds to option 4
#This outputs all names that appear in every decade as determined by the always(names) function
def all_decades(names):
    alwaysPresent = always(names)             
    print(len(alwaysPresent ), "names appear in every decade. The names are: ")
    for name in alwaysPresent:
        print( name.strip().capitalize())
    print()
#This corresponds to option 5 
#This function outputs a list of names that are decreasing in popularity over all of the years of the list
def lessPopular(names):
    alwaysPresent = always(names)
    decreasing = []
    for name in alwaysPresent:
        decrease_counter = 0 
        for i in range(0 , len(names[name])):
            if names[name][i - 1 ] < names[name][i]:
                decrease_counter += 1 
        if decrease_counter == 10:
            decreasing.append(name)
        if decrease_counter == 9 and names[name][10] == 0:
            decreasing.append(name)
    decreasing.sort()
    print(str(len(decreasing)), " names are less popular every decade.") 
    for name in decreasing:
        print(name.strip().capitalize())
    print()

#This corresponds to option 6
#This corresponds to 
def morePopular(names):
    alwaysPresent = always(names)
    increasing = []
    for name in alwaysPresent:
        increase_counter = 0 
        for i in range(1 , len(names[name])):
            if names[name][i - 1] > names[name][i]:
                increase_counter += 1 
        if increase_counter == 10:
            increasing.append(name)
    increasing.sort()
    print(str(len(increasing)), " names are more popular every decade.")
    for name in increasing:
        print(name.strip().capitalize())
    print()
    
def main():
    #This calls the create function so that the dictionary is generated
    names = create_names()
    option = 0
    #This loop prompts the user to enter their option of input
    while option < 7:
            try:
                #THis section of code prints and displays the menu for the user
                #Then it asks them for their choice
                print("Options:")
                print('Enter 1 to search for names.')
                print('Enter 2 to display data for one name.')
                print('Enter 3 to display all names that appear in only one decade.')
                print('Enter 4 to display all names that appear in all decades.')
                print('Enter 5 to display all names that are more popular in every decade.')
                print('Enter 6 to display all names that are less popular in every decade.')
                print('Enter 7 to quit.')
                print()
                option = eval(input("Pick an option from the menu to display: "))
                
                #If their choice is a valid one, one of these options is implmented
                # and outputs its results
                if option == 1:
                    name = str(input("Enter a name:"))
                    namel1 = name.lower()
                    if present(names , namel1):
                        most  = mostcommon(namel1 , names)
                        print("The match with their highest ranking decade are:")
                        print(name  , most )
                        print()
                    else:
                        print(name , "does not appear in any decade.")
                        print()
                elif option == 2 :
                        name = str(input("Enter a name:"))
                        namel2 = name.lower()
                        one_name(names, namel2)
                        print()        
                elif option == 3:
                    ordered_decade(names)
                elif option == 4:
                    all_decades(names)
                elif option == 5:
                    morePopular(names)
                elif option == 6:
                    lessPopular(names)
                if option >= 7:
                    print()
                    print('Goodbye.')
                    break   
            #If the user inputs an option that does not satisfy the needed category
            #These except statements handles the exceptions raised 
            except NameError:
                print()
                print("That is not a valid input.")
                print("Please restart the program to choose a different option.")
            except SyntaxError:
                print()
                print("That is not a valid input.")
                print("Please restart the program to choose a different option.")
            except TypeError:
                print("Strings are not valid options.")
                print("Please restart the program to choose a different option.")
main()
