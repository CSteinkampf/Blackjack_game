import os

class Player:
    def __init__(self, _name="", chips=100):
        self.name = _name
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
           
        cards_in_hand = cards_in_hand[:-2] + "."
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
        char_pos = 0

        for char in num_guess:
            if char == "-" and char_pos != 0:
                return False
            if char not in "-0123456789":
                return False
            char_pos += 1
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
            elif chip_bet < 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                chip_bet = self.get_num("Please enter a wager above 0 chips.\n")
            else:
                good_wager = True
        return chip_bet

    def place_wager(self):
        wager = self.acceptable_wager(f"Please place your bet now! Type the number of chips you would like you wager. You currently have {self.chips} chips.\n")
        self.wager = wager
        self.chips -= wager

    def atm_machine(self):
        player_choice = True
        if self.chips > 0:
            return True

        while player_choice:
            os.system('cls' if os.name == 'nt' else 'clear')
            atm_selection = input("It looks like you have ran out of chips! To go to the ATM and get more chips press enter, or press \"n\" to finish playing.\n").lower()
            
            if atm_selection == "":
                self.chips += 100
                print(f"Thank you for your purchase! You now have {self.chips} chips.")
                return True
            elif atm_selection == "n":
                return False
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                atm_selection = input("That wasn't a correct input. To go to the ATM and get more chips press enter, or press \"n\" to finish playing.\n").lower()