"""#####################################################################
# Blackjack_game_portfilio.py
# Author: Chris Steinkampf


# A text based game of blackjack hosted in terminal
# Single player vs the dealer and no AI players


# Instructional text Modified from Chris Steinkampf's text based blackjack project


# 2023-06-13
# version 1.0
# Built game and didn't use in editor documenting

# 2023-06-13
# version 1.1
# Fixed naming error when player hit a new card for their hand

# 2023-06-15
# version 1.2
# populated across many .py files for clarity

#####################################################################"""

from libs.play_game import PlayGame

def main():
    game = PlayGame()

    game.game_start()
    game.playing_game()
    
if __name__ == "__main__":
    main()

