# Terminal blackjack
# by: Ryne Smith
# started on: 8/1/2021

# Greeting
print("Welcome to table 3.")
print("Please, have a seat.")

# Required modules
import random

# Create classes and define global variables
class bcolors:
    RED = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

class Game:
    def __init__(self, num_players):
        self.num_players = num_players

class Player:
    def __init__(self, name):
        self.name = name
        self.cards_in_hand = []
        self.hand_value = 0
        self.total_score = 0

class Deck:
    def __init__(self):
        self.cards = [
        # Hearts
        [2,'♥'], [3,'♥'], [4,'♥'], [5,'♥'], [6,'♥'], [7,'♥'], [8,'♥'], [9,'♥'], [10,'♥'],
        ['J','♥'], ['Q','♥'], ['K','♥'], ['A','♥'],
        # Diamonds
        [2,'♦'], [3,'♦'], [4,'♦'], [5,'♦'], [6,'♦'], [7,'♦'], [8,'♦'], [9,'♦'], [10,'♦'],
        ['J','♦'], ['Q','♦'], ['K','♦'], ['A','♦'],
        # Clubs
        [2,'♣'], [3,'♣'], [4,'♣'], [5,'♣'], [6,'♣'], [7,'♣'], [8,'♣'], [9,'♣'], [10,'♣'],
        ['J','♣'], ['Q','♣'], ['K','♣'], ['A','♣'],
        # Spades
        [2,'♠'], [3,'♠'], [4,'♠'], [5,'♠'], [6,'♠'], [7,'♠'], [8,'♠'], [9,'♠'], [10,'♠'],
        ['J','♠'], ['Q','♠'], ['K','♠'], ['A','♠'],
        ]

    # Returns a random card popped out of the remaining cards in the deck
    def remove_card(self):
        top_card = self.cards.pop(random.randint(0, len(self.cards) - 1))

        return top_card

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    # If the card's suit is heart or diamond, render it red
    def __repr__(self):
        if self.suit == '♥' or self.suit == '♦':
            return f"| {bcolors.RED}{str(self.value)} {self.suit}{bcolors.RESET} |"
        else:
            return f"|{str(self.value)} {self.suit}| "

### TESTING ###
new_deck = Deck()
next_card = new_deck.remove_card()
new_card = Card(next_card[1], next_card[0])
print(new_card)
