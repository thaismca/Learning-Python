#import funcions from deck.py
from deck import draw_cards, show_cards, sum_hand, is_blackjack
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
    score_dealer = 0
    while score_dealer < 17:
        draw_cards(hand_dealer)
        score_dealer = sum_hand(hand_dealer)
    # get a reference to the list of cards in dealer's hand
    cards_dealer_toshow = show_cards(hand_dealer)

    # draw two starting cards to the player
    hand_player = []
    draw_cards(hand_player, 2)
    # calculate current player score
    score_player = sum_hand(hand_player)
    # get a reference to the list of cards in player's hand
    cards_player_toshow = show_cards(hand_player)

    # game loop
    game_over = False
    while not game_over:
        # calculate current player score
        score_player = sum_hand(hand_player)
        # get a reference to the updated list of cards in player's hand
        cards_player_toshow = show_cards(hand_player)

        # show round summary to player
        print(f"\n\t-> Your cards: {cards_player_toshow}, current score: {score_player}")
        print(f"\n\t-> Dealer's first card: {cards_dealer_toshow[0]}")

        # ask player input for draw or pass
        if input("\nType 'y' to draw another card, type 'n' to pass: ") == 'y':
            # draw another card to player
            draw_cards(hand_player)
            # calculate new player score
            score_player = sum_hand(hand_player)
            # get a reference to the updated list of cards in player's hand
            cards_player_toshow = show_cards(hand_player)
            # check it went over 21 -> bust, player loses -> game over
            if score_player > 21:
                print(f"\n\t-> Your cards: {cards_player_toshow}, score: {score_player}")
                print('\n\t::: BUST! ::: YOU LOSE :::')
                game_over = True
        
        else:
            # player pass -> show results -> game over
            # hands summary
            print(f"\n\t-> Your cards: {cards_player_toshow}, score: {score_player}")
            print(f"\n\t-> Dealer's cards: {cards_dealer_toshow}, score: {score_dealer}")

            # player has blackjack and dealer not -> player wins
            if is_blackjack(hand_player) and not is_blackjack(hand_dealer):
                print("\n\t::: BLACKJACK!!! YOU WIN! :::")
            # dealer has blackjack and player not -> player wins
            elif is_blackjack(hand_dealer) and not is_blackjack(hand_player):
                print("\n\t::: DEALER'S BLACKJACK!!! YOU LOSE :::")
            # player with greater hand or dealer bust -> player win
            elif score_player > score_dealer or score_dealer > 21:
                print("\n\t::: YOU WIN! :::")
            # dealer with greater hand -> player lose
            elif score_player < score_dealer:
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
