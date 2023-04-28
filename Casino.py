import random

class Player:
    def __init__(self, name, age, money = 100, chips = 0):
        self.name = name
        self.age = age
        self.money = money
        self.chips = chips
        self.discount = False

    def __repr__(self):
        print(f"This is {self.name}. He is {self.age}, and has {self.money} dollars ready to spend at the casino.")
    
    def transfer_money(self, amount):
        self.money += amount
        return f"{self.name}'s new balance is {self.money}. Remember you have to convert money to chips before you can play any of the games!"
    
    def get_chips(self):
        if self.money < 3:
            return "please add aditional funds before continuing"
        desired_chips = int(input("How many chips would you like?"))
        while desired_chips * 3 > self.money:
            desired_chips = int(input(f"Looks like {self.name} don't have enough money for that many chips, please request a smaller amount."))
        self.chips += desired_chips
        self.money -= desired_chips * 3
        print(f"Transaction complete. Your new balance is {self.chips} chips, and {self.money} dollars.")

    def discount_check(self):
        status = ""
        if self.age >= 55:
            status = "Looks like you qualify for a seniors discount, make sure to check with the machine before playing for the discount!"
            self.discount = True
        elif self.age >= 50 and self.age < 55:
            status = "Ohh you don't quite qualify for the seniors discount, getting close though!"
        else:
            status = "You don't qualify for any discounts."
        print(status)

class Slot_machine:
    def __init__(self, name, cost = 2, discount = 1):
        self.name = name
        self.cost = cost
        self.discount = discount
        self.profit = 0
        self.winnings = 0

    def __repr__(self):
        print(f"This is the {self.name} slot machine! It costs {self.cost} chips to play!")

    def apply_discount(self, player_age=0, player_discount_status=False):
        if self.cost <= 2:
            print("Sorry, this machine does not offer discounts")
            return False
        if player_age >= 55 or player_discount_status == True:
            self.cost -= self.discount
            print(f"Exciting! You qualified for a seniors discount, it now only costs {self.cost} chips to play!")
        else:
            print("You do not qualify for a discount.")

    def number_check(self, num_guess):
        for char in num_guess:
            if char not in "0123456789":
                return False
        return True

    def get_number(self):
        my_num = input("Choose a number between 1 and 10 to try win a prize! ")
        while not self.number_check(my_num):
            my_num = input("Something doesn't look right. Pick a number between 1 and 10. ")
        return int(my_num)

    def play_slots(self, payment, payout):
        winning_number = random.randint(1, 10)
        earnings = random.randint(5, 50)

        if payment < self.cost:
            print("Looks like you don't have enough chips to play this game")
            return False
        
        payment -= self.cost
        player_selection = self.get_number()

        while player_selection not in range(1, 11):
            print("That number was outside of our range!")
            player_selection = self.get_number()
                
        if player_selection == winning_number:
            payout += earnings
            self.winnings += earnings
            print(f"WOW! You just earned {earnings} dollars!")
        else:
            self.profit += self.cost
            print("That's the wrong number. Better luck next time...")

    def machine_profit(self):
        money_earned = self.profit * 3 - self.winnings
        print(f"The {self.name} slot machine has made {money_earned} dollars.")
        



        
Player1 = Player("Jimmy", 47, 500, 60)
slot_machine1 = Slot_machine("Dusty Western")

slot_machine1.play_slots(Player1.chips, Player1.money)