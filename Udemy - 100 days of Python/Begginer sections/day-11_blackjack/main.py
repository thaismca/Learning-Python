#import funcions from deck.py
from deck import draw_cards, show_cards, sum_hand
# import logo from art
from art import blackjack_logo

# to clear console
import os
clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

def start_game():
    #clear console
    clear()
    # print logo
    print(blackjack_logo)

    # draw cards to the dealer and add them 
    # continue to draw while the sum of the hand is less than 17
    hand_dealer = []
    while sum_hand(hand_dealer) < 17:
        draw_cards(hand_dealer)

    # draw two starting cards to the player
    hand_player = []
    draw_cards(hand_player, 2)

    # game loop
    game_over = False
    while not game_over:
        # show round summary to player
        print(f"\n\t-> Your cards: {show_cards(hand_player)}, current score: {sum_hand(hand_player)}")
        print(f"\n\t-> Dealer's first card: {hand_dealer[0][0]}")

        # ask player input for draw or pass
        if input("\nType 'y' to draw another card, type 'n' to pass: ") == 'y':
            # draw another card to player
            draw_cards(hand_player)
            # check it went over 21 -> bust, player loses -> game over
            if sum_hand(hand_player) > 21:
                print(f"\n\t-> Your cards: {show_cards(hand_player)}, score: {sum_hand(hand_player)}")
                print('\n\t::: BUST! ::: YOU LOSE :::')
                game_over = True
        
        else:
            # player pass -> show results -> game over
            # hands summary
            print(f"\n\t-> Your cards: {show_cards(hand_player)}, score: {sum_hand(hand_player)}")
            print(f"\n\t-> Dealer's cards: {show_cards(hand_dealer)}, score: {sum_hand(hand_dealer)}")

            # player with greater hand or dealer bust -> player win
            if sum_hand(hand_player) > sum_hand(hand_dealer) or sum_hand(hand_dealer) > 21:
                print("\n\t::: YOU WIN! :::")
            # dealer with greater hand -> player lose
            elif sum_hand(hand_player) < sum_hand(hand_dealer):
                print("\n\t::: YOU LOSE :::")
            # hands sums are equal -> draw
            else:
                print("\n\t::: DRAW :::")
            game_over = True

    # check for new game
    if input("\nType 'y' to play again or 'n' to exit: ") == 'y':
        start_game()
    else:
        return

# run game
start_game()
