import random
dealer_names = ['David', 'Andrew', 'Frank', 'Jimothy', 'Bobert', 'Liam', 'Alfred', 'Chris', 'Dale', 'Zerubbabel', 'Patrick', 'Chip', 'Edwardo', 'Piere', 'Robin', 'Linus', 'Chuck', 'Scott']

class Player:
    def __init__(self, name, age, chips=100):
        self.name = name
        self.age = age
        self.chips = chips
        self.hand = {}
        self.second_hand = {}
        self.wager = 0

    def look_at_hand(self):
        cards_in_hand = "The cards in your hand are a "

        for key, value in self.hand.items():
            for x in value:
                cards_in_hand += f"{x} of {key}, "

        cards_in_hand = cards_in_hand[:-2]
        cards_in_hand += "."
        return cards_in_hand
    
    def pick_ace(self):
        player_choice = input("You have been dealt an ace! You need to decide if you want the value of this card to be 1 or 11. Press 1 for 1, or 2 for 11")
        while answer_set == 0:
        if player_choice == 1:
            answer_set = 1
        elif player_choice == 2:
            answer_set = 1
        else:
            player_choice = input("That wasn't quite right, You need to decide if you want the value of this card to be 1 or 11. Press 1 for 1, or 2 for 11")

    def place_wager(self):
        wager = input("Please place your bet now! Type a the number of chips you would like you wager.")
       
class Dealer:
    def __init__(self, name):
        self.name = name

class Card:
    def __init__(self, name, value, suit):
        self.name = name
        self.value = value
        self.suit = suit

class Deck:
    def __init__(self):
        #hearts
        self.hearts_a = Card("ace", 1, "hearts")
        self.hearts_k = Card("king", 10, "hearts")
        self.hearts_q = Card("queen", 10, "hearts")
        self.hearts_j = Card("jack", 10, "hearts")
        self.hearts_10 = Card("ten", 10, "hearts")
        self.hearts_9 = Card("nine", 9, "hearts")
        self.hearts_8 = Card("eight", 8, "hearts")
        self.hearts_7 = Card("seven", 7, "hearts")
        self.hearts_6 = Card("six", 6, "hearts")
        self.hearts_5 = Card("five", 5, "hearts")
        self.hearts_4 = Card("four", 4, "hearts")
        self.hearts_3 = Card("three", 3, "hearts")
        self.hearts_2 = Card("two", 2, "hearts")
        #spades
        self.spades_a = Card("ace", 1, "spades")
        self.spades_k = Card("king", 10, "spades")
        self.spades_q = Card("queen", 10, "spades")
        self.spades_j = Card("jack", 10, "spades")
        self.spades_10 = Card("ten", 10, "spades")
        self.spades_9 = Card("nine", 9, "spades")
        self.spades_8 = Card("eight", 8, "spades")
        self.spades_7 = Card("seven", 7, "spades")
        self.spades_6 = Card("six", 6, "spades")
        self.spades_5 = Card("five", 5, "spades")
        self.spades_4 = Card("four", 4, "spades")
        self.spades_3 = Card("three", 3, "spades")
        self.spades_2 = Card("two", 2, "spades")
        #diamonds
        self.diamonds_a = Card("ace", 1, "diamonds")
        self.diamonds_k = Card("king", 10, "diamonds")
        self.diamonds_q = Card("queen", 10, "diamonds")
        self.diamonds_j = Card("jack", 10, "diamonds")
        self.diamonds_10 = Card("ten", 10, "diamonds")
        self.diamonds_9 = Card("nine", 9, "diamonds")
        self.diamonds_8 = Card("eight", 8, "diamonds")
        self.diamonds_7 = Card("seven", 7, "diamonds")
        self.diamonds_6 = Card("six", 6, "diamonds")
        self.diamonds_5 = Card("five", 5, "diamonds")
        self.diamonds_4 = Card("four", 4, "diamonds")
        self.diamonds_3 = Card("three", 3, "diamonds")
        self.diamonds_2 = Card("two", 2, "diamonds")
        #clubs
        self.clubs_a = Card("ace", 1, "clubs")
        self.clubs_k = Card("king", 10, "clubs")
        self.clubs_q = Card("queen", 10, "clubs")
        self.clubs_j = Card("jack", 10, "clubs")
        self.clubs_10 = Card("ten", 10, "clubs")
        self.clubs_9 = Card("nine", 9, "clubs")
        self.clubs_8 = Card("eight", 8, "clubs")
        self.clubs_7 = Card("seven", 7, "clubs")
        self.clubs_6 = Card("six", 6, "clubs")
        self.clubs_5 = Card("five", 5, "clubs")
        self.clubs_4 = Card("four", 4, "clubs")
        self.clubs_3 = Card("three", 3, "clubs")
        self.clubs_2 = Card("two", 2, "clubs")

class Stack:
    def __init__(self) -> None:
        pass

class Play_game:
    def __init__(self) -> None:
        pass

    play_round


the_deck = Deck()