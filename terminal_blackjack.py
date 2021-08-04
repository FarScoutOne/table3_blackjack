# Terminal blackjack
# by: Ryne Smith
# started on: 8/1/2021

# Greeting
# print("Welcome to table 3.")
# print("Please, have a seat.")

# Required modules
import random

# Create classes and define global variables
class bcolors:
    RED = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

class Dealer:
    def __init__(self, num_players):
        self.new_deck = Deck()
        self.hand = []
        self.players = list(range(num_players + 1))
        self.players[0] = Player('Dealer')
        self.players[1] = Player(input("Player 1, what is your name? "))


    # deals a car from the deck, prints it to command-line, and returns its value
    def deal(self):
        self.new_card = self.new_deck.remove_card()
        self.new_card_value = self.new_card[0]
        self.new_card = Card(self.new_card[0], self.new_card[1])
        #print(self.new_card, end ="  ")
        self.hand.append(self.new_card)
        return self.new_card_value

class Player:
    def __init__(self, name):
        self.name = name
        self.hand_value = 0
        self.total_score = 0

    def add_card_value(self, value):
        self.value = value
        if type(self.value) == int:
            self.hand_value += self.value
        elif self.value == 'A':
            if self.hand_value + 11 <= 21:
                self.hand_value += 11
            else:
                self.hand_value += 1
        else:
            self.hand_value += 10

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
    def __init__(self, value, suit):
        self.suit = suit
        self.value = value

    # If the card's suit is heart or diamond, render it red
    def __repr__(self):
        if self.suit == '♥' or self.suit == '♦':
            return f"| {bcolors.RED}{str(self.value)} {self.suit}{bcolors.RESET} |"
        else:
            return f"| {str(self.value)} {self.suit} |"

new_game = Dealer(1)
new_game.players[0].add_card_value(new_game.deal())
new_game.players[0].add_card_value(new_game.deal())
print(new_game.hand)
print()

# Loop until player chooses to stand or busts
hit = input("")
while new_game.players[0].hand_value <= 21 and hit == 'y':
    new_game.players[0].add_card_value(new_game.deal())
    print(new_game.hand)
    if new_game.players[0].hand_value > 21:
        print("BUST!")
        break
    print()
    hit = input("")




print(new_game.players[0].hand_value)
