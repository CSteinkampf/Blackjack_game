import random
dealer_names = ['David', 'Andrew', 'Frank', 'Jimothy', 'Bobert', 'Liam', 'Alfred', 'Chris', 'Dale', 'Zerubbabel', 'Patrick', 'Chip', 'Edwardo', 'Piere', 'Robin', 'Linus', 'Chuck', 'Scott']

class Player:
    def __init__(self, name, age, chips=100):
        self.name = name
        self.chips = chips
        self.hand = []
        self.wager = 0

    def look_at_hand(self):
        if self.hand == []:
            return "There are no cards in your hand."

        cards_in_hand = "The cards in your hand are a "

        for item in self.hand:
            cards_in_hand += item = ", "
           
        cards_in_hand = cards_in_hand[:-2]
        cards_in_hand += "."
        return cards_in_hand
    
    def pick_ace(self):
        player_choice = input("You have been dealt an ace! You need to decide if you want the value of this card to be 1 or 11. Press 1 for 1, or 2 for 11")
        while answer_set == 0:
            if player_choice == "1":
                answer_set = 1
                ace_value = 1
            elif player_choice == "2":
                answer_set = 1
                ace_value = 11
            else:
                player_choice = input("That wasn't quite right, You need to decide if you want the value of this card to be 1 or 11. Press 1 for 1, or 2 for 11")
        return ace_value

    def number_check(self, num_guess):
        for char in num_guess:
            if char not in "-0123456789":
                return False
        return True
    
    def get_num(self, text):
        num_guess = input(text)
        while not self.number_check(num_guess):
           num_guess = input("That wasn't a valid number, please try again.")
        return int(num_guess)
    
    def acceptable_wager(self, wager):
        while self.get_num(wager) > self.chips:
            wager = self.get_num(f"You don't have enough chips for a wager that high, you have {self.chips} chips. Please enter the number of chips you would like to wager.")
        return wager

    def place_wager(self):
        wager = self.get_num("Please place your bet now! Type a the number of chips you would like you wager.")
        while self.acceptable_wager(wager) <= 0:
            wager = self.get_num("Please enter a wager above 0 chips.")
        self.wager = wager
          
class Dealer:
    def __init__(self, name):
        self.name = name
        self.dealer_hand = []
        self.table_earnings = 0

class Card:
    def __init__(self, name, value, suit):
        self.name = name
        self.value = value
        self.suit = suit

    def __str__(self):
        return f"{self.name} of {self.suit}, worth {self.value} points"

class Deck:
    def __init__(self):
        card_name = {"ace": 1, "king": 10, "queen": 10, "jack": 10, "ten": 10, "nine": 9, "eight": 8, "seven": 7, "six": 6, "five": 5, "four": 4, "three": 3, "two": 2}
        card_suits = ["hearts", "diamonds", "clubs", "spades"]

        self.the_deck = []

        for suit in card_suits:
            for name, value in card_name.items():
                self.the_deck.append(Card(name, value, suit))

    def deck_list(self):
        for card in self.the_deck:
            print(card) 

    def shuffle_deck(self):
        random.shuffle(self.the_deck)

class Play_game:
    def __init__(self):
        self.player = Player("")
        self.dealer = Dealer(random.choice(dealer_names))
        self.table_deck = Deck()
        self.table_deck.shuffle_deck()
        self.round_num = 1

    def game_start(self):
        self.player.name = input(f"Hello and welcome to Blackjack! This is your dealer {self.dealer.name}, what is your name? /n")
        player_selection = input(f"Welcome to the table {self.player.name}! Would you like to get playing right away? Type Y for yes, and N for no. /n")
        player_selection = player_selection.upper()
        if player_selection == "Y":
            self.play_game()
        elif player_selection == "N":
            return "Alright, see you soon!"
        else:
            player_selection = input("That wasn't one of our options. Type Y for yes, and N for no. /n")

    def play_game(self):
        pass

    def play_round(self):
        pass

    def hit(self):
        pass

    def double_down(self):
        pass

    def split(self):
        pass

    def surrender(self):
        pass

    def payout(self):
        pass




