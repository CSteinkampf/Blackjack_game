import random
dealer_names = ['David', 'Andrew', 'Frank', 'Jimothy', 'Bobert', 'Liam', 'Alfred', 'Chris', 'Dale', 'Zerubbabel', 'Patrick', 'Chip', 'Edwardo', 'Piere', 'Robin', 'Linus', 'Chuck', 'Scott']

class Player:
    def __init__(self, name, chips=100):
        self.name = name
        self.chips = chips
        self.hand = []
        self.wager = 0

    def look_at_hand(self):
        if self.hand == []:
            return "You haven't been dealt cards yet."

        cards_in_hand = "The cards you have been dealt are a "

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
        self.chips -= wager
          
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
        self.second_hand = Player("second_hand", 0)
        self.dealer = Dealer(random.choice(dealer_names))
        self.table_deck = Deck()
        self.table_deck.shuffle_deck()
        self.round_num = 1

    def game_start(self):
        self.player.name = input(f"Hello and welcome to Blackjack! This is your dealer {self.dealer.name}, what is your name? /n")
        player_selection = input(f"Welcome to the table {self.player.name}! If you would like a reminder of the rules of Blackjack? please type Y for the rules, or if you would rather jump right into the game, type N.")
        player_selection = player_selection.upper()
        if player_selection == "Y":
            self.game_rules()
        elif player_selection == "N":
            self.play_game()
        else:
            player_selection = input("That wasn't one of our options. Type Y for yes, and N for no. /n")

    def play_game(self):
        while playing_game == True:
            self.play_round()
            playing_game = False

    def play_round(self):
        print(f"Welcome to round {self.round_num} of Blackjack.")
        self.player.place_wager()

        print("Now that all wagers have been placed we will deal the first hand.")
        for player_card in range(2):
            self.deal_card(self.player.hand)
        for dealer_card in range(2):
            self.deal_card(self.dealer.dealer_hand)

        player_hand_value = self.player_hand_check()
        if player_hand_value > 21:
            self.payout("dealer")
        elif player_hand_value == 21:
            pass

        print(f"The dealer has finished dealing the cards. The dealers face up card is a {self.dealer.dealer_hand[0]}, what would you like to do? ")

    def dealer_hand_value(self):
        has_ace = False
        hand_value = 0

        for card in self.dealer.dealer_hand:
            has_ace += card.name == "ace"
            if card.name == "ace":
                card.value = 11
            hand_value += card.value
        
        while has_ace == True:
            if hand_value >= 7:
                for card in self.dealer.dealer_hand:
                    if card.name == "ace":
                        card.value = 11
            elif has_ace == True and hand_value < 7:
                pass
        return hand_value
        
    def player_hand_check(self):
        hand_value = 0
        for card in self.player.hand:
            if card.name == "ace":
                card.value = self.player.pick_ace()
            hand_value += card.value
        return hand_value

    def deal_card(self, card_receiver):
        card_receiver.append(self.table_deck.the_deck.pop(0))

    def game_rules(self):
        while game_rules == "":
            game_rules = input("Blackjack is a betting game against the dealer. \nBefore the deal begins, each player places a bet of chips. When all the players have placed their bets, the dealer gives one card face up to each player in rotation clockwise, and then one card face up to themselves. Another round of cards is then dealt face up to each player, but the dealer takes the second card face down. Thus, each player except the dealer receives two cards face up, and the dealer receives one card face up and one card face down. \nPress enter to move on to the next section, or type anything to quit the tutorial.")
            game_rules = input("Naturals. \nIf a player's first two cards are an ace and a \"ten-card\" (a picture card or 10), giving a count of 21 in two cards, this is a natural or \"blackjack.\" If any player has a natural and the dealer does not, the dealer immediately pays that player one and a half times the amount of their bet. If the dealer has a natural, they immediately collect the bets of all players who do not have naturals, (but no additional amount). If the dealer and another player both have naturals, the bet of that player is a stand-off (a tie), and the player takes back his chips. \nPress enter to move on to the next section, or type anything to quit the tutorial.")
            game_rules = input("The Play. \nThe player to the left goes first and must decide whether to \"stand\" (not ask for another card) or \"hit\" (ask for another card in an attempt to get closer to a count of 21, or even hit 21 exactly). Thus, a player may stand on the two cards originally dealt to them, or they may ask the dealer for additional cards, one at a time, until deciding to stand on the total (if it is 21 or under), or goes \"bust\" (if it is over 21). In the latter case, the player loses and the dealer collects the bet wagered. The dealer then turns to the next player to their left and serves them in the same manner. \nPress enter to move on to the next section, or type anything to quit the tutorial.")
            game_rules = input("The Dealers Play. \nWhen the dealer has served every player, the dealers face-down card is turned up. If the total is 17 or more, it must stand. If the total is 16 or under, they must take a card. The dealer must continue to take cards until the total is 17 or more, at which point the dealer must stand. If the dealer has an ace, and counting it as 11 would bring the total to 17 or more (but not over 21), the dealer must count the ace as 11 and stand. The dealer's decisions, then, are automatic on all plays, whereas the player always has the option of taking one or more cards. \nPress enter to move on to the next section, or type anything to quit the tutorial.")
            game_rules = input("Splitting Pairs. \nIf a player's first two cards are of the same denomination, such as two jacks or two sixes, they may choose to treat them as two separate hands when their turn comes around. The amount of the original bet then goes on one of the cards, and an equal amount must be placed as a bet on the other card. The player first plays the hand to their left by standing or hitting one or more times; only then is the hand to the right played. The two hands are thus treated separately, and the dealer settles with each on its own merits. \nPress enter to move on to the next section, or type anything to quit the tutorial.")
            game_rules = input("Doubling Down \nAnother option open to the player is doubling their bet when the original two cards dealt total 9, 10, or 11. When the player's turn comes, they place a bet equal to the original bet, and the dealer gives the player just one card, which is placed face down and is not turned up until the bets are settled at the end of the hand. With two fives, the player may split a pair, double down, or just play the hand in the regular way. Note that the dealer does not have the option of splitting or doubling down. \nPress enter to move on to the next section, or type anything to quit the tutorial.")
            game_rules = input("Settlement \nA bet once paid and collected is never returned. Thus, one key advantage to the dealer is that the player goes first. If the player goes bust, they have already lost their wager, even if the dealer goes bust as well. If the dealer goes over 21, the dealer pays each player who has stood the amount of that player's bet. If the dealer stands at 21 or less, the dealer pays the bet of any player having a higher total (not exceeding 21) and collects the bet of any player having a lower total. If there is a stand-off (a player having the same total as the dealer), no chips are paid out or collected. \nPress enter to move on to the next section, or type anything to quit the tutorial.")
            game_rules = input("This has been a tutorial on Blackjack, press enter to start playing!")
            game_rules = "Join Game"
        self.play_game()

    def double_down(self):
        if self.player.chips > self.player.wager:
            self.player.wager = self.player.wager * 2
            return True
        else:
            return False

    def split(self):
        card_name = []
        for card in self.player.hand:
            card_name += card.name
        if card_name[0] == card_name[1] and self.player.wager > self.player.chips:
            self.second_hand.hand.append(self.player.hand.pop(0))
            self.second_hand.wager += self.player.wager
            self.player.chips -= self.player.wager
            return True
        else:
            return False

    def payout(self, result):
        if result == "natural":
            self.player.chips += self.player.wager * 1.5
            self.dealer.table_earnings -= self.player.wager * 1.5
            self.player.wager = 0
        if result == "player":
            self.player.chips += self.player.wager * 2
            self.dealer.table_earnings -= self.player.wager * 2
            self.player.wager = 0
        if result == "dealer":
            self.player.chips -= self.player.wager
            self.dealer.table_earnings += self.player.wager
            self.player.wager = 0
        if result == "draw":
            self.player.chips += self.player.wager
            self.player.wager = 0
        
def main():
    game = Play_game()

    while playing_game:
        playing_game = True
        dealer_hand_value = 0

        print(f"Welcome to round {game.round_num} of Blackjack.")
        game.player.place_wager()

        print("Now that all wagers have been placed we will deal the first hand.")
        for card in range(2):
            game.deal_card(game.player.hand)
            game.deal_card(game.dealer.dealer_hand)

        player_hand_value = game.player_hand_check()

        for card in game.dealer.dealer_hand:
            if card.name == "ace":
                card.value = 11
            dealer_hand_value += card.value

        if player_hand_value == 21 and dealer_hand_value == 21:
            print("A push has occured and both you and the dealer have Blackjack!")
            game.payout("draw")
        elif player_hand_value == 21 and dealer_hand_value != 21:
            print(f"You have won a natural! You have earned {game.player.wager * 1.5} Your blackjack beat the dealers hand worth {dealer_hand_value}")
            game.payout("natural")
        elif player_hand_value < 21 and dealer_hand_value == 21:
            print(f"The dealer has beaten your hand worth {player_hand_value} with their Blackjack.")
            game.payout("dealer")

        print(f"The dealer has finished dealing the cards. The dealers face up card is a {game.dealer.dealer_hand[0]}, what would you like to do?")
        



