import random
import os
import time

from .deck import Deck
from player import Player
from dealer import Dealer

dealer_names = ['David', 'Andrew', 'Frank', 'Jimothy', 'Bobert', 'Liam', 'Alfred', 'Chris', 'Dale', 'Patrick', 'Edwardo', 'Piere', 'Robin', 'Linus', 'Chuck', 'Scott', 'Johnald']

class PlayGame:
    def __init__(self):
        self.player = Player()
        self.second_hand = Player("second_hand", 0)
        self.dealer = Dealer(random.choice(dealer_names))
        self.table_deck = Deck()
        self.round_num = 1
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
        self.player_turn_results = True

    def game_start(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        rule_select = True
        self.table_deck.deck_setup()
        self.table_deck.shuffle_deck()

        self.player.name = input(f"Hello and welcome to Blackjack! This is your dealer {self.dealer.name}, what is your name? \n")
        player_selection = input(f"Welcome to the table {self.player.name}! If you would like a reminder of the rules of Blackjack? \nPlease type \"y\" for the rules, or if you would rather jump right into the game, press enter.\n").upper()
        
        while rule_select:
            if player_selection == "Y":
                self.game_rules()
                break
            elif player_selection == "":
                break
            else:
                player_selection = input("That wasn't one of our options. Type \"y\" to view the rules, or press enter to head into the game.\n")
                os.system('cls' if os.name == 'nt' else 'clear')

    def dealer_hand_value(self):
        has_ace = False
        hand_value = 0

        for card in self.dealer.dealer_hand:
            has_ace += card.name == "ace"
            hand_value += card.value
        
        while has_ace == True:
            if hand_value >= 7:
                for card in self.dealer.dealer_hand:
                    if card.name == "ace":
                        card.value = 11
                        hand_value += 10

        return hand_value
 
    def hand_check(self, selected_hand, hand_check):
        hand_value = 0
        for card in selected_hand:
            card_value = card.value
            hand_value += card_value
        hand_check

        for card in selected_hand:
            if card.name == "ace":
                print(f"You have been dealt an ace! With the ace your hand value could either be {hand_value}, or {hand_value + 10}.")
                card.value = self.player.pick_ace()
                if card.value == 11:
                    hand_value += 10
                
        print(f"Your hand's total value is {hand_value}.")

        return hand_value
  
    def deal_card(self, card_receiver):
        card_receiver.append(self.table_deck.the_deck.pop(0))

    def game_rules(self):
        rules_position = 0
        the_rules = ["Blackjack is a betting game against the dealer.\nBefore the deal begins, each player places a bet of chips.\nWhen all the players have placed their bets, the dealer gives one card face up to each player in rotation clockwise, and then one card face up to themselves.\nAnother round of cards is then dealt face up to each player, but the dealer takes the second card face down.\nThus, each player except the dealer receives two cards face up, and the dealer receives one card face up and one card face down.\nPress enter to move on to the next section, or type anything to quit the tutorial.", 
                     "Naturals.\nIf a player's first two cards are an ace and a \"ten-card\" (a picture card or 10), giving a count of 21 in two cards, this is a natural or \"blackjack.\"\nIf any player has a natural and the dealer does not, the dealer immediately pays that player one and a half times the amount of their bet.\nIf the dealer has a natural, they immediately collect the bets of all players who do not have naturals, (but no additional amount).\nIf the dealer and another player both have naturals, the bet of that player is a stand-off (a tie), and the player takes back his chips.\nPress enter to move on to the next section, or type anything to quit the tutorial.", 
                     "The Play. \nThe player goes first and must decide whether to \"stand\" (not ask for another card) or \"hit\" (ask for another card in an attempt to get closer to a count of 21, or even hit 21 exactly).\nThus, a player may stand on the two cards originally dealt to them, or they may ask the dealer for additional cards, one at a time, until deciding to stand on the total (if it is 21 or under), \nor goes \"bust\" (if it is over 21).\nIn the latter case, the player loses and the dealer collects the bet wagered.\nThe dealer then turns to the next player to their left and serves them in the same manner.\nPress enter to move on to the next section, or type anything to quit the tutorial.", 
                     "The Dealers Play. \nWhen the dealer has served every player, the dealers face-down card is turned up.\nIf the total is 17 or more, it must stand.\nIf the total is 16 or under, they must take a card.\nThe dealer must continue to take cards until the total is 17 or more, at which point the dealer must stand.\nIf the dealer has an ace, and counting it as 11 would bring the total to 17 or more (but not over 21), the dealer must count the ace as 11 and stand.\nThe dealer's decisions, then, are automatic on all plays, whereas the player always has the option of taking one or more cards.\nPress enter to move on to the next section, or type anything to quit the tutorial.", 
                     "The Dealers Play.\nWhen the dealer has served every player, the dealers face-down card is turned up.\nIf the total is 17 or more, it must stand.\nIf the total is 16 or under, they must take a card.\nThe dealer must continue to take cards until the total is 17 or more, at which point the dealer must stand.\nIf the dealer has an ace, and counting it as 11 would bring the total to 17 or more (but not over 21), the dealer must count the ace as 11 and stand.\nThe dealer's decisions, then, are automatic on all plays, whereas the player always has the option of taking one or more cards.\nPress enter to move on to the next section, or type anything to quit the tutorial.", 
                     "Splitting Pairs.\nIf a player's first two cards are of the same denomination, such as two jacks or two sixes, they may choose to treat them as two separate hands when their turn comes around.\nThe amount of the original bet then goes on one of the cards, and an equal amount must be placed as a bet on the other card.\nThe player first plays the hand to their left by standing or hitting one or more times; only then is the hand to the right played.\nThe two hands are thus treated separately, and the dealer settles with each on its own merits.\nPress enter to move on to the next section, or type anything to quit the tutorial.", 
                     "Doubling Down\nAnother option open to the player is doubling their bet when the original two cards dealt total 9, 10, or 11.\nWhen the player's turn comes, they place a bet equal to the original bet, and the dealer gives the player just one card, which is placed face down and is not turned up until the bets are settled at the end of the hand.\nWith two fives, the player may split a pair, double down, or just play the hand in the regular way.\nNote that the dealer does not have the option of splitting or doubling down.\nPress enter to move on to the next section, or type anything to quit the tutorial.", 
                     "Settlement\nA bet once paid and collected is never returned.\nThus, one key advantage to the dealer is that the player goes first.\nIf the player goes bust, they have already lost their wager, even if the dealer goes bust as well.\nIf the dealer goes over 21, the dealer pays each player who has stood the amount of that player's bet.\nIf the dealer stands at 21 or less, the dealer pays the bet of any player having a higher total (not exceeding 21) and collects the bet of any player having a lower total.\nIf there is a stand-off (a player having the same total as the dealer), no chips are paid out or collected.\nPress enter to move on to the next section, or type anything to quit the tutorial.", 
                     "This has been a tutorial on Blackjack, press enter to start playing!"]

        while rules_position < 9:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(the_rules[rules_position])
            if not input():
                rules_position += 1
            else:
                break

    def double_down(self):
        if self.player.chips > self.player.wager and self.player.player_hand_value in range(9, 12):
            double = self.player.wager
            self.player.wager += double
            self.player.chips -= double
            return True
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
        self.player.chips += (payout_select * 2)
        self.dealer.table_earnings -= (payout_select * 2)

    def dealer_win(self, payout_select):
        self.dealer.table_earnings += payout_select 
    
    def draw(self, payout_select):
        self.player.chips += payout_select
    
    def reset_deck(self):
        self.return_cards(self.player.hand)
        self.return_cards(self.second_hand.hand)
        self.return_cards(self.dealer.dealer_hand)
        self.table_deck.reset_deck()

    def return_cards(self, cards_to_return):
        while cards_to_return:
            self.table_deck.the_deck.append(cards_to_return.pop())

    def reset_game(self):
        self.reset_deck()
        self.dealer.dealer_hand_value = 0
        self.player.player_hand_value = 0
        self.second_hand.player_hand_value = 0
        self.round_num += 1

    def win_check(self, hand_select, payout_select):
        if hand_select > self.dealer.dealer_hand_value:
            print(f"Congratulations {self.player.name}! Your hand worth {hand_select} beat the dealers hand worth {self.dealer.dealer_hand_value}, and you won!")
            self.player_win(payout_select)
        elif hand_select == self.dealer.dealer_hand_value:
            print(f"Looks like this round was a draw. Both your hand and the dealers hand were worth {hand_select}.")
            self.draw(payout_select)
        else:
            print(f"Unfortunately your hand worth {hand_select} lost to the dealers hand worth {self.dealer.dealer_hand_value}. Better luck next time.")
            self.dealer_win(payout_select)

    def playing_game(self):
        self.is_playing_game = True
        os.system('cls' if os.name == 'nt' else 'clear')

        while self.is_playing_game:
            is_broke = self.player.atm_machine()
            if not is_broke:
                break

            self.playing_round()

            continue_playing = input(f"That concludes round {self.round_num}, would you like to play another round? Press enter to play another round, or type \"n\" to exit the game.\n")
            
            self.is_playing_game = self.new_round_selection(continue_playing)
            os.system('cls' if os.name == 'nt' else 'clear')
        print("Thanks for playing!")

    def new_round_selection(self, continue_input):
       self.new_round_select = True

       while self.new_round_select:
            if continue_input.lower() == "":
                self.reset_game()
                return True
            elif continue_input.lower() == "n":
                return False
            else:
                continue_input = input("Something went wrong with your answer. Press enter to play another round, or type \"n\" to exit the game.\n") 
    
    def playing_round_setup(self):
        self.is_player_turn = True
        self.is_second_hand_turn = True
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
            self.player.player_hand_value = self.hand_check(self.player.hand, self.player.look_at_hand())
            os.system('cls' if os.name == 'nt' else 'clear')
            self.has_natural = self.natural_check()

            if not self.has_natural:
                return
            
            print(f"The dealer has finished dealing the cards. The dealers face up card is a {self.dealer.dealer_hand[0]}, what would you like to do?")
            self.player_turn_results = self.player_turn()
            if not self.player_turn_results and not self.split_selection:
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
            input("A push has occured and both you and the dealer have Blackjack!\nPress enter to continue.")
            self.draw(self.player.wager)
            return False
        elif self.player.player_hand_value == 21 and self.dealer.dealer_hand_value != 21:
            input(f"You have won a natural! You have earned {self.player.wager * 1.5} chips! Your blackjack beat the dealers hand worth {self.dealer.dealer_hand_value}!\nPress enter to continue.")
            self.natural()
            return False
        elif self.player.player_hand_value < 21 and self.dealer.dealer_hand_value == 21:
            input(f"The dealer has beaten your hand worth {self.player.player_hand_value} with their Blackjack.\nPress enter to continue.")
            self.dealer_win(self.player.wager)
            return False
        return True

    def player_turn(self):
        self.is_player_turn = True
        self.player.player_hand_value = self.hand_check(self.player.hand, self.player.look_at_hand())

        while self.is_player_turn:
            self.cards_in_hand = 2

            player_selection = input("Press 1 to stand, 2 to hit, 3 to double down (if card value is 9, 10 or 11), or 4 to split (only if you have two of the same card!)\n")
            
            os.system('cls' if os.name == 'nt' else 'clear')

            match player_selection:
                case "1":
                    return True
                case "2":
                    self.select_hit()
                case "3":
                    did_double_down = self.select_double_down()
                    if did_double_down:
                        return True
                case _:
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
        self.player.player_hand_value = self.hand_check(self.player.hand, self.player.look_at_hand())
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
        if split_state:
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

            self.second_hand.player_hand_value = self.hand_check(self.second_hand.hand, self.second_hand.look_at_hand())
            player_selection = input("This is the second hand from your split! Press 1 to stand, 2 to hit.\n")

            if player_selection == "1":
                self.is_second_hand_turn = False
                return
            elif player_selection == "2":
                self.deal_card(self.second_hand.hand)
                self.second_hand.player_hand_value = self.hand_check(self.second_hand.hand, self.second_hand.look_at_hand())
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
