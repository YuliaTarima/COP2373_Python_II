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
class Deck:
    def __init__(self):
        # Initialize deck with unique cards
        # using specified ranks and suits
        self.card_list = [rank + suit
                          for suit in '\u2665\u2666\u2663\u2660'
                          for rank in 'A23456789TJQK']
        self.cards_in_play_list = []
        self.discards_list = []
        random.shuffle(self.card_list)

    def deal(self):
        # Check if the deck is empty
        if len(self.card_list) < 1:
            # check if discard pile is also empty
            if len(self.discards_list) < 1:
                print(
                    "No cards left to deal and no discards "
                    "to reshuffle.")
                # end the game
                return None
            else:
                # if discard pile is not empty
                # reshuffle the discard pile and reset the deck
                random.shuffle(self.discards_list)
                self.card_list = self.discards_list
                self.discards_list = []
                print('Reshuffling...!!!')
        # Deal a card from the deck and add it to the cards in play
        # list
        new_card = self.card_list.pop()
        self.cards_in_play_list.append(new_card)
        return new_card

    def new_hand(self):
        # Move all cards from the cards in play list to the discard
        # list
        self.discards_list += self.cards_in_play_list
        self.cards_in_play_list.clear()


def print_hand(hand):
    # Print the current hand directly
    print("Your hand:", ', '.join(hand))


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


def replace_cards(hand, deck):
    while True:
        # Print the current hand
        print_hand(hand)
        # Get valid positions from the user
        positions = get_valid_positions()
        # Replace specified cards with new cards from the deck
        for pos in positions:
            new_card = deck.deal()
            if new_card is None:
                print(
                    "Partial replacements: not enough cards "
                    "to replace all of the the selected cards.")
                return hand
            hand[pos - 1] = new_card
        # Check if the deck is empty after replacement
        if len(deck.card_list) == 0:
            print("Deck is now empty.")
            break
    return hand


def main():
    deck = Deck()

    def deal_hand():
        # Deal 5 cards for the initial hand
        hand = []
        for _ in range(5):
            card = deck.deal()
            if card is None:
                print("Not enough cards to deal a full hand.")
                return []
            hand.append(card)
        return hand

    # Deal the initial hand
    hand = deal_hand()
    if hand:
        # Allow user to replace specified cards
        # until the deck is empty
        hand = replace_cards(hand, deck)
        # Print the final hand after drawing new cards
        print("\nAfter drawing new cards:")
        print_hand(hand)


# Entry point of the program
if __name__ == "__main__":
    main()