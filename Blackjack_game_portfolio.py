import random
import os
import time
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
                os.system('cls' if os.name == 'nt' else 'clear')
                player_choice = input(f"That wasn't quite right, You need to decide if you want the value of this card to be 1 or 11. Press 1 for 1, or 2 for 11.\nYour hand value would be either {self.player_hand_value} or {self.player_hand_value + 10}.\n")
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
           os.system('cls' if os.name == 'nt' else 'clear')
           num_guess = input("That wasn't a valid number, please try again.\n")
        return int(num_guess)
    
    def acceptable_wager(self, message):
        chip_bet = self.get_num(message)
        good_wager = False
        while not good_wager:
            if chip_bet > self.chips:
                os.system('cls' if os.name == 'nt' else 'clear')
                chip_bet = self.get_num(f"You don't have enough chips for a wager that high, you have {self.chips} chips. Please enter the number of chips you would like to wager.\n")
            elif chip_bet < 0:
                os.system('cls' if os.name == 'nt' else 'clear')
                chip_bet = self.get_num("Please enter a wager above 0 chips.\n")
            else:
                good_wager = True
        return chip_bet

    def place_wager(self):
        wager = self.acceptable_wager(f"Please place your bet now! Type the number of chips you would like you wager. You currently have {self.chips} chips.\n")
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
            print("The dealer hasn't dealt the cards yet.")
            return

        cards_in_hand = "The dealer's cards are a: "

        for item in self.dealer_hand:
            current_card = item.__str__()
            cards_in_hand += current_card
            cards_in_hand += "; "
           
        cards_in_hand = cards_in_hand[:-2]
        cards_in_hand += "."
        print(cards_in_hand)

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

        #NEW VARIABLES
        self.is_playing_game = True
        self.is_playing_round = True
        self.new_round_select = True
        self.is_player_turn = True
        self.is_second_hand_turn = True
        self.split_selection = 0
        self.player_bust = False
        self.first_selection = True
        self.has_natural = True
        self.cards_in_hand = 0

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
        the_rules = ["Blackjack is a betting game against the dealer.\nBefore the deal begins, each player places a bet of chips.\nWhen all the players have placed their bets, the dealer gives one card face up to each player in rotation clockwise, and then one card face up to themselves.\nAnother round of cards is then dealt face up to each player, but the dealer takes the second card face down.\nThus, each player except the dealer receives two cards face up, and the dealer receives one card face up and one card face down.\nPress enter to move on to the next section, or type anything to quit the tutorial.", "Naturals.\nIf a player's first two cards are an ace and a \"ten-card\" (a picture card or 10), giving a count of 21 in two cards, this is a natural or \"blackjack.\"\nIf any player has a natural and the dealer does not, the dealer immediately pays that player one and a half times the amount of their bet.\nIf the dealer has a natural, they immediately collect the bets of all players who do not have naturals, (but no additional amount).\nIf the dealer and another player both have naturals, the bet of that player is a stand-off (a tie), and the player takes back his chips.\nPress enter to move on to the next section, or type anything to quit the tutorial.", "The Play. \nThe player goes first and must decide whether to \"stand\" (not ask for another card) or \"hit\" (ask for another card in an attempt to get closer to a count of 21, or even hit 21 exactly).\nThus, a player may stand on the two cards originally dealt to them, or they may ask the dealer for additional cards, one at a time, until deciding to stand on the total (if it is 21 or under), \nor goes \"bust\" (if it is over 21).\nIn the latter case, the player loses and the dealer collects the bet wagered.\nThe dealer then turns to the next player to their left and serves them in the same manner.\nPress enter to move on to the next section, or type anything to quit the tutorial.", "The Dealers Play. \nWhen the dealer has served every player, the dealers face-down card is turned up.\nIf the total is 17 or more, it must stand.\nIf the total is 16 or under, they must take a card.\nThe dealer must continue to take cards until the total is 17 or more, at which point the dealer must stand.\nIf the dealer has an ace, and counting it as 11 would bring the total to 17 or more (but not over 21), the dealer must count the ace as 11 and stand.\nThe dealer's decisions, then, are automatic on all plays, whereas the player always has the option of taking one or more cards.\nPress enter to move on to the next section, or type anything to quit the tutorial.", "The Dealers Play.\nWhen the dealer has served every player, the dealers face-down card is turned up.\nIf the total is 17 or more, it must stand.\nIf the total is 16 or under, they must take a card.\nThe dealer must continue to take cards until the total is 17 or more, at which point the dealer must stand.\nIf the dealer has an ace, and counting it as 11 would bring the total to 17 or more (but not over 21), the dealer must count the ace as 11 and stand.\nThe dealer's decisions, then, are automatic on all plays, whereas the player always has the option of taking one or more cards.\nPress enter to move on to the next section, or type anything to quit the tutorial.", "Splitting Pairs.\nIf a player's first two cards are of the same denomination, such as two jacks or two sixes, they may choose to treat them as two separate hands when their turn comes around.\nThe amount of the original bet then goes on one of the cards, and an equal amount must be placed as a bet on the other card.\nThe player first plays the hand to their left by standing or hitting one or more times; only then is the hand to the right played.\nThe two hands are thus treated separately, and the dealer settles with each on its own merits.\nPress enter to move on to the next section, or type anything to quit the tutorial.", "Doubling Down\nAnother option open to the player is doubling their bet when the original two cards dealt total 9, 10, or 11.\nWhen the player's turn comes, they place a bet equal to the original bet, and the dealer gives the player just one card, which is placed face down and is not turned up until the bets are settled at the end of the hand.\nWith two fives, the player may split a pair, double down, or just play the hand in the regular way.\nNote that the dealer does not have the option of splitting or doubling down.\nPress enter to move on to the next section, or type anything to quit the tutorial.", "Settlement\nA bet once paid and collected is never returned.\nThus, one key advantage to the dealer is that the player goes first.\nIf the player goes bust, they have already lost their wager, even if the dealer goes bust as well.\nIf the dealer goes over 21, the dealer pays each player who has stood the amount of that player's bet.\nIf the dealer stands at 21 or less, the dealer pays the bet of any player having a higher total (not exceeding 21) and collects the bet of any player having a lower total.\nIf there is a stand-off (a player having the same total as the dealer), no chips are paid out or collected.\nPress enter to move on to the next section, or type anything to quit the tutorial.", "This has been a tutorial on Blackjack, press enter to start playing!"]

        while rules_position < 9:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(the_rules[rules_position])
            user_choice = ""
            user_choice = input()
            if user_choice == "":
                rules_position += 1
            else:
                rules_position = 10

    def double_down(self):
        if self.player.chips > self.player.wager and self.player.player_hand_value in range(9, 12):
            double = self.player.wager
            self.player.wager += double
            self.player.chips -= double
            return True
        else:
            return False

    def split(self):
        card_name = []
        for card in self.player.hand:
            card_name.append(card.name)
        if card_name[0] == card_name[1] and self.player.wager < self.player.chips:
            self.second_hand.hand.append(self.player.hand.pop())
            self.second_hand.wager += self.player.wager
            self.player.chips -= self.player.wager
            return True
        else:
            return False

    def natural(self):
        self.player.chips += (self.player.wager * 1.5)
        self.dealer.table_earnings -= (self.player.wager * 1.5)
        self.player.wager = 0

    def player_win(self, payout_select):
        result_calc = payout_select
        self.player.chips += (result_calc * 2)
        self.dealer.table_earnings -= (result_calc * 2)
        payout_select = 0

    def dealer_win(self, payout_select):
        self.dealer.table_earnings += payout_select
        payout_select = 0
    
    def draw(self, payout_select):
        self.player.chips += payout_select
        payout_select = 0
    
    def reset_deck(self):
        self.return_player_cards()
        self.return_dealer_cards()
        self.return_second_hand_cards()
        self.table_deck.reset_deck()

    def return_player_cards(self):
        while self.player.hand:
            self.table_deck.the_deck.append(self.player.hand.pop())
            
    def return_second_hand_cards(self):
        while self.second_hand.hand:
            self.table_deck.the_deck.append(self.second_hand.hand.pop())
    
    def return_dealer_cards(self):
        while self.dealer.dealer_hand:
            self.table_deck.the_deck.append(self.dealer.dealer_hand.pop())

    def reset_game(self):
        self.reset_deck()
        self.dealer.dealer_hand_value = 0
        self.player.player_hand_value = 0
        self.second_hand.player_hand_value = 0
        self.round_num += 1

    def win_check(self, hand_select, payout_select):
        if hand_select > self.dealer.dealer_hand_value:
            print(f"Congradulations {self.player.name}! Your hand worth {hand_select} beat the dealers hand worth {self.dealer.dealer_hand_value}, and you won!")
            self.player_win(payout_select)
        elif hand_select == self.dealer.dealer_hand_value:
            print(f"Looks like this round was a draw. Both your hand and the dealers hand were worth {hand_select}.")
            self.draw(payout_select)
        else:
            print(f"Unfortunately your hand worth {hand_select} lost to the dealers hand worth {self.dealer.dealer_hand_value}. Better luck next time.")
            self.dealer_win(payout_select)

    #NEW METHODS
    def playing_game(self):
        self.is_playing_game = True
        os.system('cls' if os.name == 'nt' else 'clear')

        while self.is_playing_game:
            self.playing_round()

            continue_playing = input(f"That concludes round {self.round_num}, would you like to play another round? Type \"y\" for yes, or \"n\" for no.\n")
            
            self.is_playing_game = self.new_round_selection(continue_playing)

    def new_round_selection(self, continue_input):
       self.new_round_select = True

       while self.new_round_select:
            if continue_input.lower() == "y":
                self.reset_game()
                return True
            elif continue_input.lower() == "n":
                print("Thanks for playing!")
                return False
            else:
                continue_input = input("Something went wrong with your answer, please type \"y\" to play another round, or \"n\" to stop playing.\n") 
    
    def playing_round_setup(self):
        self.player_turn = True
        self.second_hand_turn = True
        self.dealer.dealer_hand_value = 0
        self.split_selection = 0
        self.player_bust = False
        self.first_selection = True

    def init_card_deal(self):
        for card in range(2):
                self.deal_card(self.dealer.dealer_hand)
                self.deal_card(self.player.hand)

    def playing_round(self):
        self.is_playing_round = True
        while self.is_playing_round:
            self.playing_round_setup()

            print(f"Welcome, {self.player.name}, to round {self.round_num} of Blackjack.")
            self.player.place_wager()

            print("\nNow that all wagers have been placed we will deal the first hand.")
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            self.init_card_deal()
            self.dealer_ace_value_check()
            self.has_natural = self.natural_check()

            if not self.has_natural:
                return
            
            print(f"The dealer has finished dealing the cards. The dealers face up card is a {self.dealer.dealer_hand[0]}, what would you like to do?")
            player_turn_results = self.player_turn()
            if not player_turn_results and not self.split_selection:
                return
            
            if self.split_selection:
                self.second_hand_turn()

            print(f"Okay it is the dealers turn.\nThe dealer flips his second card over, which is a {self.dealer.dealer_hand[1]}. The dealers hand value is {self.dealer.dealer_hand_value}.\n")
            dealer_result = self.dealers_turn()
            if not dealer_result:
                return
            
            print("\nAlright let's compare hands!\n")
            self.compare_hands()
            self.is_playing_round = False

    def dealer_ace_value_check(self):
        for card in self.dealer.dealer_hand:
                if card.name == "ace":
                    card.value = 11
                self.dealer.dealer_hand_value += card.value
            
    def natural_check(self):
        if self.player.player_hand_value == 21 and self.dealer.dealer_hand_value == 21:
            print("A push has occured and both you and the dealer have Blackjack!")
            self.draw(self.player.wager)
            return False
        elif self.player.player_hand_value == 21 and self.dealer.dealer_hand_value != 21:
            print(f"You have won a natural! You have earned {self.player.wager * 1.5} chips! Your blackjack beat the dealers hand worth {self.dealer.dealer_hand_value}")
            self.natural()
            return False
        elif self.player.player_hand_value < 21 and self.dealer.dealer_hand_value == 21:
            print(f"The dealer has beaten your hand worth {self.player.player_hand_value} with their Blackjack.")
            self.dealer_win(self.player.wager)
            return False

    def player_turn(self):
        self.is_player_turn = True

        while self.is_player_turn:
            self.cards_in_hand = 2

            player_selection = input("Press 1 to stand, 2 to hit, 3 to double down (if card value is 9, 10 or 11), or 4 to split (only if you have two of the same card!)\n")
            time.sleep(0.5)
            os.system('cls' if os.name == 'nt' else 'clear')
            if player_selection == "1":
                return True
            elif player_selection == "2":
                self.select_hit()
            elif player_selection == "3":
                did_double_down = self.select_double_down()
                if did_double_down:
                    return True
            elif player_selection == "4":
                self.select_split()   
            else:
                print("That wasn't a correct input.")
                self.player.look_at_hand()
                print(f"Your hand's total value is {self.player.player_hand_value}.")
                    
            if self.player.player_hand_value > 21:
                print(f"Oh no! Your hand value is {self.player.player_hand_value}, which means you have bust and lost your bet.")
                self.dealer_win(self.player.wager)
                if self.split_selection == 0:
                    return False
                else:
                    self.player_bust = True
                    return True

    def select_hit(self):
        self.deal_card(self.player.hand)
        self.player.player_hand_value = self.player_hand_check()
        self.cards_in_hand += 1

    def select_double_down(self):
        double_down_state = self.double_down()
        if double_down_state:
            self.deal_card(self.player.hand)
            self.player.player_hand_value = self.player_hand_check()
            return True
        else: 
            print("looks like your cards don't have the right value to double down, try another option.")
            self.player.look_at_hand()
            print(f"Your hand's total value is {self.player.player_hand_value}.")
            return False

    def select_split(self):
        if self.split_selection > 0:
            print("You've already split this round, try another option.")
            self.player.look_at_hand()
            return
        
        split_state = self.split()
        if split_state == True:
            self.deal_card(self.player.hand)
            self.deal_card(self.second_hand.hand)
            self.player.player_hand_value = self.player_hand_check()
            self.split_selection += 1
        else:
            print("looks like your cards don't match so you can't split, try another option.")
            self.player.look_at_hand()
            print(f"Your hand's total value is {self.player.player_hand_value}.")
            
    def second_hand_turn(self):
        self.is_second_hand_turn = True
        input("we will now move on to the second hand, press enter to continue!\n")

        while self.is_second_hand_turn and len(self.second_hand.hand) > 0:
            os.system('cls' if os.name == 'nt' else 'clear')

            self.second_hand.player_hand_value = self.second_hand_check()
            player_selection = input("This is the second hand from your split! Press 1 to stand, 2 to hit.\n")

            if player_selection == "1":
                self.is_second_hand_turn = False
                return
            elif player_selection == "2":
                self.deal_card(self.second_hand.hand)
                self.second_hand.player_hand_value = self.second_hand_check()
            else:
                player_selection = "That wasn't a correct input. Press 1 to stand, 2 to hit."

            if self.second_hand.player_hand_value > 21:
                break

        if self.second_hand.player_hand_value > 21:
            print(f"Oh no! Your hand value is {self.second_hand.player_hand_value}, which means you have bust and lost your bet.")
            self.dealer_win(self.second_hand.wager)
            self.is_second_hand_turn = True
            return

    def dealers_turn(self):
        while self.dealer.dealer_hand_value < 17:
            self.deal_card(self.dealer.dealer_hand)
            new_card = self.dealer.dealer_hand[-1]
            self.dealer.dealer_hand_value += new_card.value
            print(f"The dealer has dealt themselves a new card, the {new_card.__str__()}. The dealers hand value is {self.dealer.dealer_hand_value}.")
            
        if self.dealer.dealer_hand_value > 21:
            print(f"the dealer has bust with a hand value of {self.dealer.dealer_hand_value}, and you have won the round!")
            self.player_win(self.player.wager)
            if self.is_second_hand_turn:
                self.player_win(self.second_hand.wager)
            return False
        return True

    def compare_hands(self):
        if not self.player_bust:
            self.win_check(self.player.player_hand_value, self.player.wager)

        if not self.is_second_hand_turn:
            print("\nNow we will check the second hand against the dealer!")
            self.win_check(self.second_hand.player_hand_value, self.second_hand.wager)

def main():
    game = Play_game()

    game.game_start()
    game.playing_game()


main()      

