import random
dealer_names = ['David', 'Andrew', 'Frank', 'Jimothy', 'Bobert', 'Liam', 'Alfred', 'Chris', 'Dale', 'Zerubbabel', 'Patrick', 'Chip', 'Edwardo', 'Piere', 'Robin', 'Linus', 'Chuck', 'Scott']

class Player:
    def __init__(self, name, chips=100):
        self.name = name
        self.chips = chips
        self.hand = []
        self.wager = 0
        self.player_hand_value = 0

    def look_at_hand(self):
        if self.hand == []:
            print("You haven't been dealt cards yet.")
            return

        cards_in_hand = "The cards you have been dealt are a: "

        for item in self.hand:
            current_card = item.__str__()
            cards_in_hand += current_card
            cards_in_hand += "; "
           
        cards_in_hand = cards_in_hand[:-2]
        cards_in_hand += "."
        print(cards_in_hand)
    
    def pick_ace(self):
        answer_set = 0

        player_choice = input("You need to decide if you want the value of this card to be 1 or 11. Press 1 for 1, or 2 for 11\n")
        while answer_set == 0:
            if player_choice == "1":
                answer_set = 1
                ace_value = 1
            elif player_choice == "2":
                answer_set = 1
                ace_value = 11
            else:
                player_choice = input("That wasn't quite right, You need to decide if you want the value of this card to be 1 or 11. Press 1 for 1, or 2 for 11\n")
        return ace_value

    def number_check(self, num_guess):
        for char in num_guess:
            if char not in "-0123456789":
                return False
        if num_guess == "":
            return False
        return True
    
    def get_num(self, text):
        num_guess = input(text)
        while not self.number_check(num_guess):
           num_guess = input("That wasn't a valid number, please try again.\n")
        return int(num_guess)
    
    def acceptable_wager(self, message):
        chip_bet = self.get_num(message)
        good_wager = False
        while not good_wager:
            if chip_bet > self.chips:
                chip_bet = self.get_num(f"You don't have enough chips for a wager that high, you have {self.chips} chips. Please enter the number of chips you would like to wager.\n")
            elif chip_bet < 0:
                chip_bet = self.get_num("Please enter a wager above 0 chips.\n")
            else:
                good_wager = True
        return chip_bet

    def place_wager(self):
        wager = self.acceptable_wager("Please place your bet now! Type the number of chips you would like you wager.\n")
        self.wager = wager
        self.chips -= wager
          
class Dealer:
    def __init__(self, name):
        self.name = name
        self.dealer_hand = []
        self.table_earnings = 0
        self.dealer_hand_value = 0

    def dealer_dealt_cards(self):
        if self.hand == []:
            return "The dealer hasn't dealt the cards yet."

        cards_in_hand = f"The dealer's cards are a "

        for item in self.dealer_hand:
            cards_in_hand += item + ", "
           
        cards_in_hand = cards_in_hand[:-2]
        cards_in_hand += "."
        return cards_in_hand

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

    def reset_deck(self):
        for card in self.the_deck:
            if card.name == "ace":
                card.value = 1
        self.shuffle_deck()

class Play_game:
    def __init__(self):
        self.player = Player("")
        self.second_hand = Player("second_hand", 0)
        self.dealer = Dealer(random.choice(dealer_names))
        self.table_deck = Deck()
        self.table_deck.shuffle_deck()
        self.round_num = 1

    def game_start(self):
        self.player.name = input(f"Hello and welcome to Blackjack! This is your dealer {self.dealer.name}, what is your name? \n")
        player_selection = input(f"Welcome to the table {self.player.name}! If you would like a reminder of the rules of Blackjack? please type \"y\" for the rules, or if you would rather jump right into the game, type \"n\".\n")
        player_selection = player_selection.upper()
        if player_selection == "Y":
            self.game_rules()
        elif player_selection == "N":
            pass
        else:
            player_selection = input("That wasn't one of our options. Type Y for yes, and N for no. \n")

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
            card_value = card.value
            hand_value += card_value
        self.player.look_at_hand()

        for card in self.player.hand:
            if card.name == "ace":
                print(f"You have been dealt an ace! With the ace your hand value could either be {hand_value}, or {hand_value + 10}.")
                card.value = self.player.pick_ace()
                if card.value == 11:
                    hand_value += 10
                
        print(f"Your hand's total value is {hand_value}.")

        return hand_value
    
    def second_hand_check(self):
        hand_value = 0
        for card in self.second_hand.hand:
            card_value = card.value
            hand_value += card_value
        self.second_hand.look_at_hand()

        for card in self.second_hand.hand:
            if card.name == "ace":
                print(f"You have been dealt an ace! With the ace your hand value could either be {hand_value}, or {hand_value + 10}.")
                card.value = self.second_hand.pick_ace()
                if card.value == 11:
                    hand_value += 10
            
        print(f"Your hand's total value is {hand_value}.")

        return hand_value

    def deal_card(self, card_receiver):
        card_receiver.append(self.table_deck.the_deck.pop(0))

    def game_rules(self):
        rules_position = 0
        the_rules = ["Blackjack is a betting game against the dealer. \nBefore the deal begins, each player places a bet of chips. When all the players have placed their bets, the dealer gives one card face up to each player in rotation clockwise, and then one card face up to themselves. Another round of cards is then dealt face up to each player, but the dealer takes the second card face down. Thus, each player except the dealer receives two cards face up, and the dealer receives one card face up and one card face down. \nPress enter to move on to the next section, or type anything to quit the tutorial.", "Naturals. \nIf a player's first two cards are an ace and a \"ten-card\" (a picture card or 10), giving a count of 21 in two cards, this is a natural or \"blackjack.\" If any player has a natural and the dealer does not, the dealer immediately pays that player one and a half times the amount of their bet. If the dealer has a natural, they immediately collect the bets of all players who do not have naturals, (but no additional amount). If the dealer and another player both have naturals, the bet of that player is a stand-off (a tie), and the player takes back his chips. \nPress enter to move on to the next section, or type anything to quit the tutorial.", "The Play. \nThe player to the left goes first and must decide whether to \"stand\" (not ask for another card) or \"hit\" (ask for another card in an attempt to get closer to a count of 21, or even hit 21 exactly). Thus, a player may stand on the two cards originally dealt to them, or they may ask the dealer for additional cards, one at a time, until deciding to stand on the total (if it is 21 or under), or goes \"bust\" (if it is over 21). In the latter case, the player loses and the dealer collects the bet wagered. The dealer then turns to the next player to their left and serves them in the same manner. \nPress enter to move on to the next section, or type anything to quit the tutorial.", "The Dealers Play. \nWhen the dealer has served every player, the dealers face-down card is turned up. If the total is 17 or more, it must stand. If the total is 16 or under, they must take a card. The dealer must continue to take cards until the total is 17 or more, at which point the dealer must stand. If the dealer has an ace, and counting it as 11 would bring the total to 17 or more (but not over 21), the dealer must count the ace as 11 and stand. The dealer's decisions, then, are automatic on all plays, whereas the player always has the option of taking one or more cards. \nPress enter to move on to the next section, or type anything to quit the tutorial.", "The Dealers Play. \nWhen the dealer has served every player, the dealers face-down card is turned up. If the total is 17 or more, it must stand. If the total is 16 or under, they must take a card. The dealer must continue to take cards until the total is 17 or more, at which point the dealer must stand. If the dealer has an ace, and counting it as 11 would bring the total to 17 or more (but not over 21), the dealer must count the ace as 11 and stand. The dealer's decisions, then, are automatic on all plays, whereas the player always has the option of taking one or more cards. \nPress enter to move on to the next section, or type anything to quit the tutorial.", "Splitting Pairs. \nIf a player's first two cards are of the same denomination, such as two jacks or two sixes, they may choose to treat them as two separate hands when their turn comes around. The amount of the original bet then goes on one of the cards, and an equal amount must be placed as a bet on the other card. The player first plays the hand to their left by standing or hitting one or more times; only then is the hand to the right played. The two hands are thus treated separately, and the dealer settles with each on its own merits. \nPress enter to move on to the next section, or type anything to quit the tutorial.", "Doubling Down \nAnother option open to the player is doubling their bet when the original two cards dealt total 9, 10, or 11. When the player's turn comes, they place a bet equal to the original bet, and the dealer gives the player just one card, which is placed face down and is not turned up until the bets are settled at the end of the hand. With two fives, the player may split a pair, double down, or just play the hand in the regular way. Note that the dealer does not have the option of splitting or doubling down. \nPress enter to move on to the next section, or type anything to quit the tutorial.", "Settlement \nA bet once paid and collected is never returned. Thus, one key advantage to the dealer is that the player goes first. If the player goes bust, they have already lost their wager, even if the dealer goes bust as well. If the dealer goes over 21, the dealer pays each player who has stood the amount of that player's bet. If the dealer stands at 21 or less, the dealer pays the bet of any player having a higher total (not exceeding 21) and collects the bet of any player having a lower total. If there is a stand-off (a player having the same total as the dealer), no chips are paid out or collected. \nPress enter to move on to the next section, or type anything to quit the tutorial.", "This has been a tutorial on Blackjack, press enter to start playing!"]

        while rules_position < 8:
            print(the_rules[rules_position])
            user_choice = ""
            user_choice = input()
            if user_choice == "":
                rules_position += 1
            else:
                rules_position = 10

    def double_down(self):
        if self.player.chips > self.player.wager and self.player.player_hand_value in range(9, 12):
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

    def natural(self):
        self.player.chips += self.player.wager * 1.5
        self.dealer.table_earnings -= self.player.wager * 1.5
        self.player.wager = 0

    def player_win(self):
        self.player.chips += self.player.wager * 2
        self.dealer.table_earnings -= self.player.wager * 2
        self.player.wager = 0

    def dealer_win(self):
        self.player.chips -= self.player.wager
        self.dealer.table_earnings += self.player.wager
        self.player.wager = 0
    
    def draw(self):
        self.player.chips += self.player.wager
        self.player.wager = 0
    
    def reset_deck(self):
        self.return_player_cards()
        self.return_dealer_cards()
        self.return_second_hand_cards()
        self.table_deck.reset_deck()

    def return_player_cards(self):
        for value in range(0, len(self.player.hand)):
            self.table_deck.the_deck.append(self.player.hand.pop(value))
            
    def return_second_hand_cards(self):
        for value in range(0, len(self.second_hand.hand)):
            self.table_deck.the_deck.append(self.second_hand.hand.pop(value))
    
    def return_dealer_cards(self):
        for value in range(0, len(self.dealer.hand)):
            self.table_deck.the_deck.append(self.dealer.hand.pop(value))

   

game = Play_game()


ace_of_hearts = Card("ace", 1, "hearts")
king_of_spades = Card("king", 10, "spades")
eight_of_clubs = Card("eight", 8, "clubs")

game.player.hand.append(eight_of_clubs)
game.player.hand.append(ace_of_hearts)

game.player_hand_check()

game.player.look_at_hand()