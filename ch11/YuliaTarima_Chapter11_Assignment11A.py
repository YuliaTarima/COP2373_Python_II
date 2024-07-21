# YuliaTarima_Chapter11_Assignment11A

"""
Using the Deck object presented in Section 11.5,
this program deals a Poker hand of five cards.
Then it prompts the user to enter a series of numbers (e.g.: 1, 3, 5)
replaces the cards at the given positions during a draw phrase
and prints the result of drawing the new cards.
"""
import random


# Deck class manages the deck of cards, including shuffling,
# dealing, and resetting the hand
class Deck():
    def __init__(self, n_decks=1):
        # Initialize deck with number of decks (defaulting to one)
        # of  unique cards with specified ranks and suits
        self.card_list = [num + suit
                          for suit in '\u2665\u2666\u2663\u2660'
                          for num in 'A23456789TJQK'
                          for deck in range(n_decks)]
        self.cards_in_play_list = []
        self.discards_list = []
        random.shuffle(self.card_list)

    def deal(self):
        # Check if the deck is empty
        if len(self.card_list) < 1:
            # if so reshuffle the discard pile
            random.shuffle(self.discards_list)
            # and reset the deck
            self.card_list = self.discards_list
            self.discards_list = []
            print('Reshuffling...!!!')

        # Deal a card from the deck
        # and add it to the cards in play list
        new_card = self.card_list.pop()
        self.cards_in_play_list.append(new_card)
        return new_card

    def new_hand(self):
        # Move all cards from the cards in play list
        # to the discard list
        self.discards_list += self.cards_in_play_list
        self.cards_in_play_list.clear()


# Function to validate user input
def get_valid_positions():
    while True:
        # Prompt user to enter positions of cards to be replaced
        to_replace = input(
            "\nEnter the positions (1-5) of the cards you want to "
            "replace, separated by spaces: ")
        try:
            # Convert the input positions to a list of integers
            positions = list(map(int, to_replace.split()))
            # Check if all positions are valid
            if all(1 <= pos <= 5 for pos in positions):
                return positions
            else:
                print("Invalid positions. Please enter numbers "
                      "between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter numbers separated "
                  "by spaces.")


# Function to deal a hand of 5 cards from the deck
# and store them in a dictionary
def deal_hand(deck):
    current_hand = {i + 1: deck.deal() for i in range(5)}
    return current_hand


# Function to print the dictionary values as a string
def print_hand_as_string(hand):
    hand_str = ', '.join(str(card) for card in hand.values())
    return {hand_str}


def main():
    # initialize the deck using six-deck shoe
    deck = Deck(6)

    # deal the initial hand of 5 cards
    hand = deal_hand(deck)
    print("Initial hand:", print_hand_as_string(hand))

    positions = get_valid_positions()
    for pos in positions:
        hand[pos] = deck.deal()
    print("Hand after drawing new cards:", print_hand_as_string(hand))


# Entry point of the program
if __name__ == "__main__":
    main()