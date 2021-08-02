# Terminal blackjack
# by: Ryne Smith
# started on: 8/1/2021

'''
This is a simple game of blackjack that plays in the command-line terminal.
There are still a few aspects that need to be decided:
- Will more than one player be able to play against the dealer/computer?
- Will the deck be shuffled/randomized and prior to a hand, or will the only one card be determined at a time? (Schrodinger's deck)
- How many hands can be used with one deck?
- Will a manual be provided?
- How will scoring be determined? (a point per hand won vs betting)
'''

# Greeting
print("Welcome to table 3.")
print("Please, have a seat.")

# Create classes and define global variables
class Player:
    def __init__(self, name):
        self.name = name
        self.cards_in_hand = []
        self.hand_value = 0
        self.total_score = 0

class Card:
    # suit
    # value

class Deck:
    # top_card
    # number of cards remaining
