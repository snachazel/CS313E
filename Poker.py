# -*- coding: utf-8 -*-
# =============================================================================
# #  File: Poker.py

#  Description: A program that simulates a hand of poker.

#  Student's Name:Stephen Nachazel

#  Student's UT EID: sdn443

#  Course Name: CS 313E 

#  Unique Number: 51345

#  Date Created: 9 /24 / 2018

#  Date Last Modified: 9 /28/2018
# =============================================================================
import random

#This class constructs the object of a card in order to reate a deck
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

#This object represents an actual game of poker being playeed
class Poker: 
    
    def __init__( self, num_players = 2 , num_cards = 5 ):
        self.deck = Deck()
        self.deck.shuffle()
        self.all_hands = []
        self.num_players = num_players
        self.num_cards_in_hand = num_cards
        
        #This loop sets up num_cards amount of empty hands
        for i in range(num_players):
            self.all_hands.append([])
        
        #this loop deals num_cards to each empty hand by 
        #going round robin style
        for n in range(num_cards):
            for m in range(num_players):
                self.all_hands[m].append(self.deck.deal())
    
    #This method conducts a game of poker           
    def play(self):
        
        points = []
        rank = []
        order = []
        
        
        for i in range(len(self.all_hands)):
            
            sorted_hand = sorted(self.all_hands[i] , reverse = True)
            self.all_hands[i] = sorted_hand
            hand_str = ' '
           
            for card in sorted_hand:
                hand_str = hand_str + str(card) + ' '
            
            print( "Player " + str(i + 1 ) + ":" + hand_str)
            
            if self.is_royal(self.all_hands[i])> 0:
                points.append(self.is_royal(self.all_hands[i]))
                rank.append("Player" + str(i + 1 ) + ":" + "Royal Flush")
                order.append(10)
                continue
            
            elif self.is_straight_flush(self.all_hands[i]) > 0:
                points.append(self.straight_flush(self.all_hands[i]))
                rank.append("Player " + str(i + 1 ) + ": " + " Straight Flush")
                order.append(9)
                continue
            
            elif self.is_four_kind(self.all_hands[i]) > 0:
                points.append(self.is_four_kind(self.all_hands[i]))
                rank.append("Player " + str(i + 1 ) + ": " + " Four of a Kind")
                order.append(8)
                continue
            
            elif self.is_full_house(self.all_hands[i]) > 0:
                points.append(self.is_full_house(self.all_hands[i]))
                rank.append("Player " + str(i + 1 ) + ": " + " Full House")
                order.append(7)
                continue
            
            elif self.is_flush(self.all_hands[i]) > 0:
                points.append(self.is_flush(self.all_hands[i]))
                rank.append("Player " + str(i + 1 ) + ": " + " Flush")
                order.append(6)
                continue
           
            elif self.is_straight(self.all_hands[i]) > 0:
                points.append(self.is_straight(self.all_hands[i]))
                rank.append("Player " + str(i + 1 ) + ": " + " Straight")
                order.append(5)
                continue
            
            elif self.is_three_kind(self.all_hands[i]) > 0:
                points.append(self.is_three_kind(self.all_hands[i]))
                rank.append("Player " + str(i + 1 ) + ": " + " Three of a Kind")
                order.append(4)
                continue
            
            elif self.is_two_pair(self.all_hands[i]) > 0:
                points.append(self.is_two_pair(self.all_hands[i]))
                rank.append("Player " + str(i + 1 ) + ": " + " Two Pair")
                order.append(3)
                continue
            elif self.is_one_pair(self.all_hands[i]) > 0:
                points.append(self.is_one_pair(self.all_hands[i]))
                rank.append("Player " + str(i + 1 ) + ": " + " One Pair")
                order.append(2)
                continue
            else:
                points.append(self.is_high_card(self.all_hands[i]))
                rank.append("Player " + str(i + 1 ) + ": " + " High Card")
                order.append(1)
                continue
        
        #This loop prints each of the players hands
        print()
        for i in range(self.num_players):
            print(rank[i])
        
        #This conditional says that if there isa single winner, 
        #They are printed out as the winner
        if order.count(max(order)) == 1:
            win = points.index(max(points))
            print()
            print("Player " + str(win + 1) + " is the winner.")
       
        #this conditional says that if there is a tie,
        #the ties are printed out in descending order of points
        else:
            print()
            ties = []
            for i in range (len(self.all_hands)):
                if order[i] == max(order): 
                    ties.append([ i , points[i]])
            ties = sorted( ties , key = lambda x:x[1] , reverse = True)
            for i in range(len(ties)):
                print( "Player " + str(ties[i][0] + 1) + " ties")
    #This function determines if the hand is a royal flush   
    def is_royal(self, hand):
        h = 10
        same_suit = True
        for i in range(len(hand) - 1):
        
            same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)
       
        if not same_suit:
        
            return 0
        
        rank_order = True 
        for i in range(len(hand)):
        
            rank_order = rank_order and (hand[i].rank == 14- i )
        if not rank_order:
       
            return 0 
       
        if same_suit and rank_order:
       
            return  h * 15**5 + (hand[0].rank * 15**4) + (hand[1].rank * 15**3 )+ (hand[2].rank * 15**2) + (hand[3].rank * 15) + hand[4].rank
   
    #This function determines  if the hand is a straight flush
    #by checking suit and rank
    def is_straight_flush (self, hand):
        h = 9
        same_suit = True
        for i in range(len(hand) - 1):
            same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)
        if not same_suit:
            return 0
        rank_order = True 
        for i in range(len(hand) - 1):
            rank_order = rank_order and (hand[i + 1].rank - hand[i].rank == 1 )
        if not rank_order:
            return 0
        else: 
            return  h * 15**5 + (hand[0].rank * 15**4) + (hand[1].rank * 15**3 )+ (hand[2].rank * 15**2) + (hand[3].rank * 15) + hand[4].rank
    
    #This function checks if a hand is a four of a kind
    def is_four_kind (self, hand):
        h= 8 
        
        four_kind = False 
        for i in range(len(hand) - 3 ):
            same_card = (hand[i].rank == hand[i +1].rank == hand[i+2].rank == hand[i +3].rank)
            if same_card:
                four_kind = True
                break
       
        if not four_kind:
        
            return 0
       
        if four_kind:
            
            if (hand[0].rank == hand[1].rank == hand[2].rank == hand[3].rank):
            
                return  h * 15**5 + (hand[0].rank * 15**4) + (hand[1].rank * 15**3 )+ (hand[2].rank * 15**2) + (hand[3].rank * 15) + hand[4].rank
           
            if (hand[1].rank == hand[2].rank == hand[3].rank == hand[4].rank):
            
                return  h * 15**5 + (hand[1].rank * 15**4) + (hand[2].rank * 15**3 )+ (hand[3].rank * 15**2) + (hand[4].rank * 15) + hand[0].rank

    #This function chekcs if a hand is a full house
    #that is a three of a kind and a pair 
    def is_full_house (self, hand):
        h = 7 
      
        v1 = (hand[0].rank == hand[1].rank) and (hand[2].rank == hand[3].rank == hand[4].rank)
        v2 = (hand[0].rank == hand[1].rank == hand[2].rank ) and ( hand[3].rank == hand[4].rank)
       
        if v1 :           
          
            return  h * 15**5 + (hand[2].rank * 15**4) + (hand[3].rank * 15**3 )+ (hand[4].rank * 15**2) + (hand[0].rank * 15) + hand[1].rank
       
        elif v2:
           
            return  h * 15**5 + (hand[0].rank * 15**4) + (hand[1].rank * 15**3 )+ (hand[2].rank * 15**2) + (hand[3].rank * 15) + hand[4].rank
       
        else:
            return 0 
    
    #This function checks if a hand is a flush
    #that is a hand with all same suit
    def is_flush (self, hand):
        h = 6
        same_suit = True
        
        for i in range(len(hand) - 1):
        
            same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)
       
        if not same_suit:
            return 0
       
        else:
            return  h * 15**5 + (hand[0].rank * 15**4) + (hand[1].rank * 15**3 )+ (hand[2].rank * 15**2) + (hand[3].rank * 15) + hand[4].rank
    
    #This function chekcs if a hand is a straight, which 
    #means is numeric cards in descending order by 1
    def is_straight (self, hand):
        
        h= 5
        rank_order = True 
       
        for i in range(len(hand) - 1):
            rank_order = rank_order and (hand[i + 1].rank - hand[i].rank == 1 )
       
        if not rank_order:
            return 0
       
        else:
            return  h * 15**5 + (hand[0].rank * 15**4) + (hand[1].rank * 15**3 )+ (hand[2].rank * 15**2) + (hand[3].rank * 15) + hand[4].rank

    #This function chekcs if a hand has three of the same card 
    def is_three_kind (self, hand):
        h = 4 
        three_kind = False 
        
        for i in range(len(hand) - 2 ):
            same_card = (hand[i].rank == hand[i +1].rank == hand[i+2].rank)
           
            if same_card:
                three_kind = True
                break
       
        if not three_kind:
            return 0
       
        if three_kind:
            if (hand[0].rank == hand[1].rank == hand[2].rank):
              
                return  h * 15**5 + (hand[0].rank * 15**4) + (hand[1].rank * 15**3 )+ (hand[2].rank * 15**2) + (hand[3].rank * 15) + hand[4].rank
           
            elif (hand[1].rank == hand[2].rank == hand[3].rank):
               
                return  h * 15**5 + (hand[1].rank * 15**4) + (hand[2].rank * 15**3 )+ (hand[3].rank * 15**2) + (hand[0].rank * 15) + hand[4].rank
           
            elif (hand[2].rank == hand[3].rank == hand[4].rank):
              
                return  h * 15**5 + (hand[2].rank * 15**4) + (hand[3].rank * 15**3 )+ (hand[4].rank * 15**2) + (hand[0].rank * 15) + hand[1].rank
   
   #This function chekcs if a hand has two pairs in it
    def is_two_pair (self, hand):
        h = 3
        v1 = (hand[0].rank == hand[1].rank) and (hand[2].rank == hand[3].rank)
        
        v2 = (hand[0].rank == hand[1].rank) and (hand[3].rank == hand[4].rank)
        
        v3 = (hand[1].rank == hand[2].rank) and (hand[3].rank == hand[4].rank)
        
        if v1 :
            
            return  h * 15**5 + (hand[0].rank * 15**4) + (hand[1].rank * 15**3 )+ (hand[2].rank * 15**2) + (hand[3].rank * 15) + hand[4].rank
        
        elif v2:
            
            return  h * 15**5 + (hand[0].rank * 15**4) + (hand[1].rank * 15**3 )+ (hand[3].rank * 15**2) + (hand[4].rank * 15) + hand[2].rank
       
        elif v3:
            
            return  h * 15**5 + (hand[1].rank * 15**4) + (hand[2].rank * 15**3 )+ (hand[3].rank * 15**2) + (hand[4].rank * 15) + hand[0].rank
      
        else:
            return 0
        
    #This function chekcs if there is a single pair in a hand 
    def is_one_pair ( self, hand):
      h = 2
      is_pair = False
      for i in range( len(hand) - 1):
          if hand[i].rank == hand[i+1].rank:
              is_pair = True
              break
      if (not is_pair):
           return 0
      if (is_pair):
          if (hand[0].rank == hand[1].rank):
              
            return  h * 15**5 + (hand[0].rank * 15**4) + (hand[1].rank * 15**3 )+ (hand[2].rank * 15**2) + (hand[3].rank * 15) + hand[4].rank
         
          elif (hand[1].rank == hand[2].rank):
              
            return  h * 15**5 + (hand[1].rank * 15**4) + (hand[2].rank * 15**3 )+ (hand[0].rank * 15**2) + (hand[3].rank * 15) + hand[4].rank
          
          elif (hand[2].rank == hand[3].rank):
              
            return  h * 15**5 + (hand[2].rank * 15**4) + (hand[3].rank * 15**3 )+ (hand[0].rank * 15**2) + (hand[1].rank * 15) + hand[4].rank
          
          elif (hand[3].rank == hand[4].rank):
              
            return  h * 15**5 + (hand[3].rank * 15**4) + (hand[4].rank * 15**3 )+ (hand[0].rank * 15**2) + (hand[1].rank * 15) + hand[2].rank
    
    #This function returns the points of the hand if there are no other hands possible
    def is_high_card (self, hand):
        h = 1 
        return  h * 15**5 + (hand[0].rank * 15**4) + (hand[1].rank * 15**3 )+ (hand[2].rank * 15**2) + (hand[3].rank * 15) + hand[4].rank

# do not remove this line above main()                        
if __name__ == '__main__':
    
    def main():
            #The number of players must be an integer between 2 and 6
            num_players = int(input("Enter number of players: "))
            print()
            while ((num_players < 2) or (num_players > 6 )):
                print()
                num_players = int(input("Enter number of players: "))
            game = Poker( num_players )
            game.play()
    
    main()

