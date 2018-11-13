# -*- coding: utf-8 -*-
# =============================================================================
# #  File: TestCipher.py
# 
# #  Description: This is a program that tests the Caesar and Vignere ciphers on provided phrases.
# 
# #  Student Name:Stephen Nachazel 
# 
# #  Student UT EID: sdn443
# 
# #  Course Name: CS 313E
# 
# #  Unique Number: 51345
# 
# #  Date Created: 9/6/2018
# 
# #  Date Last Modified: 9 / 10  / 2018 
# =============================================================================

# takes a single string as input parameter and returns a string
def substitution_encode ( strng ):
    #This segment of code initilizaes the string and lists for the function to use
    cipher = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o', 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z']
    cipher = ['q' , 'a', 'z' , 'w' , 's' , 'x' , 'e' , 'd' , 'c' , 'r' , 'f' , 'v' , 't' , 'g' , 'b' , 'y' , 'h' , 'n' , 'u' , 'j' , 'm' , 'i' , 'k' , 'o' , 'l' , 'p']
    strng = strng.lower()
    pass_phrase = ""
    pieces = len(strng)
    
    #This loop takes the ord value of each character in the phrase and shifts it to the cipher index
    #It then adds the character to the string to be returned
    for i in range( 0 , pieces):
        if strng[i] in cipher:
           cipher_idx = ord(strng[i]) - ord('a')
           pass_phrase += cipher[cipher_idx]
        else:
           pass_phrase += strng[i]
    return(pass_phrase)

# takes a single string as input parameter and returns a string   
def substitution_decode ( strng ):
    #This segment of code initilizaes the string and lists for the function to use
    cipher = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o', 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z']
    cipher = ['q' , 'a', 'z' , 'w' , 's' , 'x' , 'e' , 'd', 'c' , 'r' , 'f' , 'v' , 't' , 'g' , 'b' , 'y' , 'h' , 'n' , 'u' , 'j' , 'm' , 'i' , 'k' , 'o' , 'l' , 'p']
    strng = strng.lower()
    decode_phrase = ""
    pieces = len(strng)
    
    #This loop takes the shifted indices and shifts them back in order 
    #to return the proper decoded phrase 
    for j in range(0, pieces):
        if strng[j] in cipher:
            plain_idx = cipher.index(strng[j])
            decode_phrase += cipher[plain_idx]
        else: 
            decode_phrase += strng[j]    
    return(decode_phrase)
# takes two strings as input parameter and returns a string
def vigenere_encode ( strng, passwd ):
    #This segment of code initilizaes the string and lists for the function to use
    cipher = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o', 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z']
    strng = strng.lower()
    passwd = passwd.lower()
    
    #THis section of code measures the string length and extends the password phrase 
    #to be at least as long as the string in order to use its indices for encryption 
    strng_length = len(strng)
    passwd_cycle = passwd * strng_length
    vignere_helper = ''
    vignere_encoded_phrase = ''
    
    #This loop creates the password phrase of the correct length as the password 
    #using the extended version previously created
    cycle_idx = 0 
    for h in range(0 , strng_length):
        if strng[h] in cipher:
            vignere_helper += passwd_cycle[cycle_idx]
            cycle_idx += 1 
        else:
            vignere_helper += strng[h]
            
     #This loop encodes the original phrase using the vigenere method of adding the character indices 
    #and taking the corresponding index for the cipher text list        
    for i in range(0 , strng_length):
        if strng[i] in cipher:
            cipher_idx = (cipher.index(strng[i]) + cipher.index(vignere_helper[i])) % 26
            vignere_encoded_phrase += cipher[cipher_idx]
        else:
            vignere_encoded_phrase += strng[i]
    
    #This function returns the Vignere encoded phrase
    return( vignere_encoded_phrase)
            
# takes two strings as input parameter and returns a string
def vigenere_decode ( strng, passwd ):
    #This segment of code initilizaes the string and lists for the function to use
    cipher = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o', 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z']
    strng = strng.lower()
    passwd = passwd.lower()
    
    #This section of code measures the string length and extends the password phrase 
    #to be at least as long as the string in order to use its indices for encryption
    strng_length = len(strng)
    passwd_cycle = passwd * strng_length
    vignere_helper = ''
    vignere_decoded_phrase = ''
    
    #this loop prepares the helper phrase for the vignere cipher by creating a phrase of equal length to the 
    # phrase to be decoded in order to sum their inidices for use in decoding 
    cycle_idx2 = 0 
    for m in range(0 , strng_length):
        if strng[m] in cipher:
            vignere_helper += passwd_cycle[cycle_idx2]
            cycle_idx2 += 1 
        else:
            vignere_helper += strng[m]
            
    #This loop incorporates the password phrase extended to the length of the phrase to be decoded 
    #and then undoes the encoding operation in order to recreate the original phrase
    for v in range(0 , strng_length):
        if strng[v] in cipher:
            cipher_idx = (cipher.index(strng[v]) - cipher.index(vignere_helper[v])) % 26
            vignere_decoded_phrase += cipher[cipher_idx]
        else:
            vignere_decoded_phrase += strng[v]
   
    #This function returns the decoded phrase according to the vignere cipher and the corresponding password  
    return( vignere_decoded_phrase)
    
def main():
  
  # open file for reading
  in_file = open("./cipher.txt", "r")

  # print header for substitution cipher
  print("Substitution Cipher")
  print()

  # read line to be encoded
  line = in_file.readline()
  line = line.strip()
  line = line.lower()

  # encode using substitution cipher
  encoded_str = substitution_encode(line)

  # print result
  print("Plain Text to be Encoded: " + line)
  print("Encoded Text: " + encoded_str)
  print()

  # read line to be decoded
  line = in_file.readline()
  line = line.strip()
  line = line.lower()

  # decode using substitution cipher
  decoded_str = substitution_decode (line)

  # print result
  print ("Encoded Text to be Decoded: " + line)
  print ("Decoded Plain Text: " + decoded_str)
  print ()

  # print header for vigenere cipher
  print ("Vigenere Cipher")
  print ()

  # read line to be encoded and pass phrase
  line = in_file.readline()
  line = line.strip()
  line = line.lower()

  passwd = in_file.readline()
  passwd = passwd.strip()
  passwd = passwd.lower()

  # encode using vigenere cipher
  encoded_str = vigenere_encode (line, passwd)

  # print result
  print("Plain Text to be Encoded: " + line)
  print("Pass Phrase (no spaces allowed): " + passwd)
  print("Encoded Text: " + encoded_str)
  print()

  # read line to be decoded and pass phrase
  line = in_file.readline()
  line = line.strip()
  line = line.lower()

  passwd = in_file.readline()
  passwd = passwd.strip()
  passwd = passwd.lower()

  # decode using vigenere cipher
  decoded_str = vigenere_decode (line, passwd)

  # print result
  print ("Encoded Text to be Decoded: " + line)
  print ("Pass Phrase (no spaces allowed): " + passwd)
  print ("Decoded Plain Text: " + decoded_str)
  print ()

  # close file
  in_file.close()
main()
