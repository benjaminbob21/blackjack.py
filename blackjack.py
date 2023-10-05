from random import randint
# DEFINING NEEDED FUNCTIONS
# Prints the given card's official name in the form "Drew a(n) ___".
# If the input card is invalid, prints "BAD CARD"
#
# Parameters:
#   card_rank: The numeric representation of a card (1-13)
#
# Return:
#   none
def print_card_name(card_rank):
    if card_rank == 8:
        print("Drew an " + str(card_rank))
    elif card_rank == 1:
        print("Drew an Ace")
    elif card_rank == 11:
        print("Drew a Jack")
    elif card_rank == 12:
        print("Drew a Queen")
    elif card_rank == 13:
        print("Drew a King")
    elif (1 < card_rank < 8) or (8 < card_rank < 11):
        print("Drew a " + str(card_rank))
    else:
        print("BAD CARD")
# Draws a new random card, prints its name, and returns its value.
#
# Parameters:
#   none
#
# Return:
#   an int representing the value of the card. All cards are worth
#   the same as the card_rank except Jack, Queen, King, and Ace.
def draw_card():
    card_rank = randint(1,13)
#We assign conditions for different values of first card drawn
    if card_rank == 8:
        print("Drew an " + str(card_rank))
    elif card_rank == 1:
        print("Drew an Ace")
        card_rank = 11
    elif card_rank == 11:
        print("Drew a Jack")
        card_rank = 10
    elif card_rank == 12:
        print("Drew a Queen")
        card_rank = 10
    elif card_rank == 13:
        print("Drew a King")
        card_rank = 10
    else:
        print("Drew a " + str(card_rank))
    card_rank = int(card_rank)
    return card_rank
# Prints the given message formatted as a header. A header looks like:
# -----------
# message
# -----------
#
# Parameters:
#   message: the string to print in the header
#
# Return:
#   none
def print_header(message):
    print("-----------")
    print(message)
    print("-----------")
# Prints turn header and draws a starting hand, which is two cards.
#
# Parameters:
#   name: The name of the player whose turn it is.
#
# Return:
#   The hand total, which is the sum of the two newly drawn cards.
def draw_starting_hand(name):
    name = name + " TURN"
    print("-----------\n" + name + "\n-----------")
    card1 = draw_card()
    card2 = draw_card()
    result = card1 + card2
    return result
    # Implement draw_starting_hand function here
# Prints the hand total and status at the end of a player's turn.
#
# Parameters:
#   hand_value: the sum of all of a player's cards at the end of their turn.
#
# Return:
#   none
def print_end_turn_status(hand_value):
    print("Final hand: " + str(hand_value) + ".")
    if hand_value == 21:
        print("BLACKJACK!")
    elif hand_value > 21 and hand_value <= 31:
        print("BUST.")

# Prints the end game banner and the winner based on the final hands.
#
# Parameters:
#   user_hand: the sum of all cards in the user's hand
#   dealer_hand: the sum of all cards in the dealer's hand
#
# Return:
#   none
def print_end_game_status(user_hand, dealer_hand):
    print_header("GAME RESULT")
    if (user_hand > 21) or (user_hand < dealer_hand):
        print("Dealer wins!")
    elif user_hand > dealer_hand or (dealer_hand > 21):
        print("You win!")
    elif user_hand == dealer_hand:
        print("Push.")

# ACTUAL GAME
user_hand = draw_starting_hand("YOUR")
# Put conditions for the user to decide to continue drawing
response = "y"
while user_hand < 21 and not(response == "n"):
  response = input("You have " + str(user_hand) + ". Hit (y/n)? ")
  if response == "y":
    card_player = draw_card()
    user_hand = user_hand + card_player
    response = "y"
  elif response == "n":
    response = "n"
  else:
    print("Sorry I didn't get that.")
    response = "y"
# Print the end status for the user
print_end_turn_status(user_hand)

# Print header and generate 2 values for the dealer
dealer_hand = draw_starting_hand("DEALER")
# Create while loop to continue generating values for dealer when total dealer card is less than 17
while dealer_hand < 17:
  print("Dealer has " + str(dealer_hand) + ".")
  card_x = draw_card()
  dealer_hand = dealer_hand + card_x
# Print end status for dealer
print_end_turn_status(dealer_hand)

#  Finally print end game status and decide who wins or if they push
print_end_game_status(user_hand, dealer_hand)