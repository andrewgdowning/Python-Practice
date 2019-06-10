'''
Blackjack
Version 0.01
Author: Andrew Downing
'''
#Import modules
import random

#Define constants
NUMBER_OF_CARDS = 52
SUITS = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
CARDS = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
         'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': [1, 10]}

class Card:
    """
    Card object consisting of suit and card rank
    card = the card name and accompanying value as part of a dictionary pair
    suit = the suit the card belongs to in tuple format
    """

    def __init__(self, suit, card):
        self.suit = suit
        self.card = card
        self.card_value = CARDS[self.card]

    def __str__(self):
        """
        Define how a card should print with card, suit and value
        """
        return str(self.card + " of " + self.suit + " with value of " + str(self.card_value))

class Deck:
    """
    Deck object containing 52 ranom cards as a list object
    Shuffle method will shuffle the 52 card deck and list object using the random module
    Hit method on the deck will draw a random card and remove from the deck list object
    """

    def __init__(self):
        self.deck_cards = []
        for suit in SUITS:
            for card in CARDS:
                self.deck_cards.append(Card(suit, card).__str__())

    def __str__(self):
        """ Print string for deck """
        return str(self.deck_cards)

    def shuffle(self):
        """ Shuffle method """
        random.shuffle(self.deck_cards)

    def deal_card(self):
        return self.deck_cards.pop()

class Player:
    """
    Player object for players playing BlackJac
    name = payer name
    """

    def __init__(self, name):
        self.name = name
        self.hand = []
        self.hand_value = []
        self.chips = 100

    def __str__(self):
        return str(self.name + " has " + str(self.chips) + " chips ")

    def return_hand_value(self):
        """ Method to return the value of the players current hand """
        return sum(self.hand_value)

    def return_chip_value(self):
        """ method to return the current number of chips """
        return sum(self.chips)

    def place_bet(self, bet):
        """ method to reduce the number of chips by the bet amount """
        self.chips -= bet

    def add_to_hand(self, card):
        """
        Method to add a card to current hand
        card = card object passed from deck
        """
        self.hand.append(card)
        self.hand_value += 10


#test deck
test_deck = Deck()
test_deck.shuffle()
print(test_deck.deal_card())

player_one = Player('Andrew')
print(player_one)



"""
dealers_deck = Deck()
dealers_deck.shuffle()
print(dealers_deck)

card_list = []
for suit in SUITS:
    for card in CARDS:
        card_list.append(Card(suit, card).__str__())

print(card_list)
"""
