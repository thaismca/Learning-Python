# deck to be used in the blackjack game
deck = {
    "A": 11,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10,
}


# functions related to deck manipulation
import random 

def draw_cards(hand, num = 1):
    '''It receives the hand to where the cards must be added and the number of cards to be drawn (this number defaults to 1).
Draws random cards from the deck until it fulfils the quantity that was passed, and returns the hand updated with the new card(s)'''
    cards = random.sample(list(deck.items()), num)
    hand += cards
    return hand

def show_cards(hand):
    '''It receives a hand and returns a list with the face value of all the cards in it'''
    # display_hand = []
    # for card in hand:
    #     display_hand.append(card[0])
    # return display_hand
    return [card[0] for card in hand]

def sum_hand(hand):
    '''It receives a hand and returns the sum of the values of all cards in it'''
    # sum the value for all cards in the hand
    # hand_total = 0
    # for card in hand:
    #     hand_total += card[1]
    hand_total = sum(card[1] for card in hand)
    #checking for aces in hands with total over 21, to convert the value from 11 to 1
    if hand_total > 21:
        aces = [card for card in hand if card[0] == "A"]
        for _ in aces:
            if hand_total > 21:           
                hand_total -= 10
    # return total
    return hand_total

def is_blackjack(hand):
    '''It receives a hand and returns true if it has a blackjack and false if not'''
    return sum_hand(hand) == 21 and len(hand) == 2


# note: next iteration will involve implementing this as a class