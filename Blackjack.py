# -*- coding: utf-8 -*-

# =============================================================================
# # File: Blackjack.py
# 
#   # Description: A program that simulates a game of blackjack 
# 
#   # Student's Name: Stephen Nachazel 
# 
#   # Student's UT EID: sdn443
#   
#   # Course Name: CS 313E 
# 
#   # Unique Number: 51345
# 
#   # Date Created: 9 /29/18
# 
#   # Date Last Modified: 10/1 / 2018
# =============================================================================

import random 
  
class Card:
    
    #these class variables are meant to represent ranks and suits of cards 
    RANKS = (2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 11 , 12 , 13 , 14)

    SUITS = ('C' , 'D'  , 'H' , 'A')
    
    #constructor
    def __init__(self , rank = 12  , suit = 'H'):
        
        if rank in Card.RANKS:
            self.rank = rank
        else:
            self.rank = 12
        
        if suit in Card.SUITS:
            self.suit = suit
        else:
            self.suit = 'H'
   
    #This method prints a string representation of a card    
    def __str__(self):
        
        #This segment of code takes the ranks of the face cards and turns them
        #into their depicted values
        if self.rank == 14:
            rank = 'A'
        elif self.rank == 13:
            rank = 'K'
        elif self.rank == 12:
            rank = 'Q'
        elif self.rank == 11:
            rank = 'J'
        else:
            rank = str(self.rank)
        
        return( rank + self.suit)

    #testing equality of cards 
    def __eq__(self , other):
        return(self.rank == other.rank)
        
    def __ne__(self , other):
        return(self.rank != other.rank)
        
    def __lt__(self , other):
        return self.rank < other.rank
    
    def __gt__(self , other):
        return self.rank > other.rank
    
    def __le__(self , other):
        return self.rank <= other.rank
    
    def __ge__(self , other):
        return self.rank >= other.rank

#this class constructs a deck object composed of card objects
class Deck(object):
    
    #constructor 
    def __init__(self , n = 1 ):
        
        #This loop constructs a deck of n repitions of a 52 card deck
        self.deck = []
        for i in range(n):
           
            for suit in Card.SUITS:
            
                for rank in Card.RANKS:
                
                    card = Card(rank, suit)
                    self.deck.append(card)
    
    #This method shuffles a deck                 
    def shuffle(self):
        
        random.shuffle(self.deck)
    
    #This method deals a card o a player by removing it from the dek    
    def deal(self):
        
        if (len(self.deck) == 0):
           
            return None
        
        else:
          
            return self.deck.pop(0)

#this defines a player object which is a list of card objects       
class Player (object):
  # cards is a list of Card objects
  def __init__ (self, cards):
    self.cards = cards

  # when a player hits append a card
  def hit (self, card):
    self.cards.append (card)

  # count the points in the Players's hand
  def get_points (self):
      
    count = 0
    for card in self.cards:
        if (card.rank > 9):
            count += 10
     
        elif (card.rank == 1):
            count += 11
     
        else:
            count += card.rank

    # deduct 10 if Ace is there and needed as 1
    for card in self.cards:
        
      if (count <= 21):
        break
    
      elif (card.rank == 1):
        count = count - 10

    return count

  # does the player have blackjack
  def has_blackjack (self):
    return (len(self.cards) == 2) and (self.get_points() == 21)

  # this method returns a string representation of the hand of each player object
  def __str__ (self):
      
        hand = " "
        points = self.get_points()
        for card in self.cards:
            hand = hand + " " + str(card)
        point_counter = " - " + str(points) + " points"
        return hand + point_counter

#the dealer is a player object with additional attributes and different methods 
class Dealer (Player):
    
  def __init__ (self, cards):
    Player.__init__ (self, cards)
    self.show_one_card = True

  # over-ride the hit() function in the parent class
  def hit (self, deck):
    self.show_one_card = False
    while (self.get_points() < 17):
      self.cards.append (deck.deal())

  # return a string showing just one card if not hit yet
  def __str__ (self):
      
    if (self.show_one_card):
      return str(self.cards[0])
  
    else:
      return Player.__str__ (self)

#this creates the game of blackjack as an object 
class Blackjack (object):
    
  def __init__ (self, num_players = 1):
    self.deck = Deck()
    self.deck.shuffle()

    # create the number of Player objects
    self.num_players = num_players
    self.player_list = []
    
    #this loop appends two cards to all players hands in the game 
    for i in range (self.num_players):
      player = Player([self.deck.deal(), self.deck.deal()])
      self.player_list.append(player)

    # create the Dealer object
    # dealer also gets two cards
    self.dealer = Dealer ([self.deck.deal(), self.deck.deal()])

  def play (self):
    # print the cards that each player has
    print()
    for i in range (self.num_players):
      print ('Player ' + str(i + 1) + ' : ' + str(self.player_list[i]))

    # print the cards that the dealer has
    print ('Dealer : ' + str(self.dealer))

    # each player hits until he says no
    player_points = []
    for i in range (self.num_players):
      loop = True
      while loop:
       choice = input ('Player ' + str(i +1) + ' do you want to hit? [y / n ]: ')
       if choice in ('y', 'Y'):
         (self.player_list[i]).hit(self.deck.deal())
         points = (self.player_list[i]).get_points()
         print ('Player ' + str(i + 1) + ' :' + str(self.player_list[i]) ,end = " ")
         if (points > 21):
            loop = False
            break
            print()
       else:
         loop = False
         break
         print()
      player_points.append((self.player_list[i]).get_points())

    # dealer's turn to hit
    self.dealer.hit(self.deck)
    dealer_points = self.dealer.get_points()
    print()
    print ('Dealer :' + str(self.dealer))
    print()
   #this loop goes through all of the player's points 
   #and determines the outcome of each player relative to the dealer 
    for i in range(len(self.player_list)):
        if (player_points[i] > 21):
            print ('Player ' + str(i +1) +' loses')
        elif (self.player_list[i].has_blackjack() or dealer_points > 21):
           print ('Player ' + str(i +1) +' wins')
        elif (self.dealer.has_blackjack()):
            print ('Player ' + str(i +1) +' loses') 
        elif (dealer_points <= 21) and (dealer_points > player_points[i]):
          print ('Player ' + str(i +1) +' loses')
        elif (dealer_points < player_points[i] and player_points[i] <= 21):
          print ('Player ' + str(i +1) +' wins')
        elif (dealer_points == player_points[i]):
          print ('Player ' + str(i +1) +' ties')

def main():
    
  num_players = int (input ('Enter number of players: '))
  while (num_players < 1 or num_players > 6):
    num_players = int (input ('Enter number of players: '))

  # create the Balckjack object
  game = Blackjack (num_players)

  # start the game
  game.play()
    
main()

