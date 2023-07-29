############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.

##############################################################################################

# Here, my code

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.

import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def random_cards(cards):
    return random.sample(cards, 2)

cards_dealer = random_cards(cards)
cards_player = random_cards(cards)
bet = input("How much are you going to bet? $ ")


def sum_cards(cards_list):
    return int(cards_list[0]) + int(cards_list[1])


def sum_cards_plus(cards_list):
    return int(cards_list[0]) + int(cards_list[1]) + int(cards_list[2])


while sum_cards(cards_dealer) == sum_cards(cards_player):
    print(f"Total value of Dealer Cards: {sum_cards(cards_dealer)}")
    print(f"Total value of Player Cards: {sum_cards(cards_player)}")
    print("Draw")
    cards_dealer = random_cards(cards)
    cards_player = random_cards(cards)

if sum_cards(cards_dealer) > sum_cards(cards_player):
    print(f"Total value of Dealer Cards: {sum_cards(cards_dealer)}")
    print(f"Total value of Player Cards: {sum_cards(cards_player)}")

    new_card = input("Would you like a new card? Y or N\n")
  
    if new_card.lower() == 'y':
      card_plus = random.sample(cards, 1)
      card_plus_transformation = card_plus[0]
      cards_player.append(card_plus_transformation)
      
      if sum_cards_plus(cards_player) > 21:
        print(f"Total value of Dealer Cards: {sum_cards(cards_dealer)}")
        print(f"Total value of Player Cards: {sum_cards_plus(cards_player)}")
        print(f"You lose $ {bet}!")
      else:
        if sum_cards(cards_dealer) > sum_cards_plus(cards_player):
          print(f"Total value of Dealer Cards: {sum_cards(cards_dealer)}")
          print(f"Total value of Player Cards: {sum_cards_plus(cards_player)}")
          print(f"You lose $ {bet}")
        else:
          print(f"Total value of Dealer Cards: {sum_cards(cards_dealer)}")
          print(f"Total value of Player Cards: {sum_cards_plus(cards_player)}")
          print(f"You win $ {bet}")
          
    elif new_card.lower() == 'n':
      print(f"You lose $ {bet}")
      
else:
    print(f"Total value of Dealer Cards: {sum_cards(cards_dealer)}")
    print(f"Total value of Player Cards: {sum_cards(cards_player)}")
    print(f"You win $ {bet}!")
