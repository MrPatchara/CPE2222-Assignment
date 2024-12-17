import random

A = ['\u2660', '\u2665', '\u2666', '\u2663']  
B = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

deck = [rank1 + rank2 for rank2 in A for rank1 in B]

def calculate_score(hand):
    score = 0
    for card in hand:
        rank = card[:-1]  
        if rank == 'A':
            score += 1  # A มีคะแนน 1
        elif rank in ['J', 'Q', 'K']:
            score += 10  # J, Q, K มีคะแนน10
        else:
            score += int(rank)  # ไพ่ที่เป็น (2-10) 
    return score

def deal_cards(deck):
    random.shuffle(deck)  
    dealer_hand = [deck.pop(), deck.pop()]  
    player_hand = [deck.pop(), deck.pop()]  
    return dealer_hand, player_hand


def display_result(dealer_score, player_score):
    if player_score > dealer_score:
        return "WIN"
    elif player_score == dealer_score:
        return "DRAW"
    else:
        return "LOST"

def play_game():
    dealer_hand, player_hand = deal_cards(deck)
    
    dealer_score = calculate_score(dealer_hand)
    player_score = calculate_score(player_hand)
    
    print("Welcome to the card game") 
    print("*"*40)  
    print("Dealer:")
    print(f"The first card is: {dealer_hand[0]}")
    print(f"The second card is: {dealer_hand[1]}")
    print(f"Score: {dealer_score}")
    print("*"*40) 
    print("Player:")
    print(f"The first card is: {player_hand[0]}")
    print(f"The second card is: {player_hand[1]}")
    print(f"Score: {player_score}")
    print("*"*40) 
    result = display_result(dealer_score, player_score)
    print(f"RESULT: {result}")
    
play_game()
