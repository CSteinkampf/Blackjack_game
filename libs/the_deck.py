import random

from libs.card import Card

class Deck:
    def __init__(self):
        self.card_names = {"ace": 1, "king": 10, "queen": 10, "jack": 10, "ten": 10, "nine": 9, "eight": 8, "seven": 7, "six": 6, "five": 5, "four": 4, "three": 3, "two": 2}
        self.card_suits = ["hearts", "diamonds", "clubs", "spades"]
        self.the_deck = []

    def deck_setup(self):
        for suit in self.card_suits:
            for name, value in self.card_names.items():
                self.the_deck.append(Card(name, value, suit))

    def deck_list(self):
        for card in self.the_deck:
            print(card) 

    def shuffle_deck(self):
        random.shuffle(self.the_deck)

    def reset_deck(self):
        for card in self.the_deck:
            if card.name == "ace":
                card.value = 1
        self.shuffle_deck()

