#Creating a game of comparing cards 

#Class to initalise the players of the game
class Player(object):
    def __init__(self, name):
        """card, a string
            Adds valid card to the player's hand"""
        #Create name and empty hand for cards
        self.hand = []
        self.name = name
    def _get_name_(self):
        #Returns the Player's name
        return self.name
    def _get_card(self, card):
        #to get card from the shuffler
        if card != None :
            self.hand.append(card)
    def _return_card_(self, card):
        #to give away your card from the hand
        self.hand.remove(card)
    def _size_hand_(self):
        #to know how many cards are there in your hand
        return len(self.hand)

import random
#defining the playing cards in the game
class carddeck(object):
    def __init__(self):
        #all four groups of the cards (Hearts, Spades, Clubs and Diamonds)
        hearts = "2H,3H,4H,5H,6H,7H,8H,9H"
        diamonds = "2D,3D,4D,5D,6D,7D,8D,9D"
        spades = "2S,3S,4S,5S,6S,7S,8S,9S"
        clubs = "2C,3C,4C,5C,6C,7C,8C,9C"
        self.deck = hearts.split(',')+diamonds.split(',')+spades.split(',')+clubs.split(',')

    def _get_card(self):
        #get a card from the carddeck
        #if there are no cards then we can't play anymore
        if (len(self.deck) < 1 ):
            return None
        #choosing a card from the deck randomly
        card = random.choice(self.deck)
        self.deck.remove(card)
        return card #removing the card from the deck

    def compare_cards(self,card1,card2):
        #comparing the two cards to find which one has more value
        #the comparision :
        # Spades > Hearts > Diamonds > Clubs
        if (card1[0] > card2[0]) :
            return card1
        elif (card1[0] < card2[0]):
            return card2
        elif (card1[1] < card2[1]):
            return card1
        else :
            return card2

#initializing the main game
Player1 = input('Enter the name of player 1 : ')
player1 = Player(Player1)
Player2 = input('Enter the name of player 2 : ')
player2 = Player(Player2)

deck = carddeck()
i = 1
import time
#conditions for the game
while (True) :
	time.sleep(0.5)
	print('\n')
	print('-----------------------------')
	print('Round',i,'/17')
	i += 1
	player1_card = deck._get_card()
	player2_card = deck._get_card()
	player1._get_card(player1_card)
	player2._get_card(player2_card)
	if (player1_card == None or player2_card == None):
		print("Game over. No more cards in the deck")
		print(Player1,"has", player1._size_hand_())
		print(Player2,"has", player2._size_hand_())
		print("Who won ? ")
		if (player1._size_hand_() > player2._size_hand_()):
			print(Player2,"wins!")
		elif (player1._size_hand_() < player2._size_hand_()):
			print(Player1,"wins!")
		else :
			print("A Tie")
		break
	else :
		print(Player1,":",player1_card)
		print(Player2,":",player2_card)
		if (deck.compare_cards(player1_card,player2_card) == player1_card):
			player2._get_card(player1_card)
			player1._return_card_(player1_card)
		else :
			player1._get_card(player2_card)
			player2._return_card_(player2_card)








