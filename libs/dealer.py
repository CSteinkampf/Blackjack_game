class Dealer:
    def __init__(self, _name):
        self.name = _name
        self.dealer_hand = []
        self.table_earnings = 0
        self.dealer_hand_value = 0
    
    def dealer_dealt_cards(self):
        if self.dealer_hand == []:
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