#3.จงเขียนโปรแกรมการเล่นเกมส์ไพ่ โดยใช้สำรับไพ่มาตรฐานมีจำนวนทั้งหมด 52 ใบ (Standard 52 card desk)

import random
# สร้างชุดไพ่
suits = ['\u2660', '\u2665', '\u2666', '\u2663']  # โพดำ, โพแดง, ข้าวหลามตัด, ดอกจิก
ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

# สร้างสำรับไพ่ทั้งหมด
deck = [rank + suit for suit in suits for rank in ranks]

# ฟังก์ชั่นในการคำนวณคะแนนของไพ่
def calculate_score(hand):
    score = 0
    for card in hand:
        rank = card[:-1]  # เอาแค่ตัวอักษรแรก (เช่น A, 2, J เป็นต้น)
        if rank == 'A':
            score += 1  # ไพ่ A มีคะแนนเท่ากับ 1
        elif rank in ['J', 'Q', 'K']:
            score += 10  # ไพ่ J, Q, K มีคะแนนเท่ากับ 10
        else:
            score += int(rank)  # ไพ่ที่เป็นตัวเลข (2-10) จะใช้ค่าตามตัวเลข
    return score

# ฟังก์ชั่นในการแจกไพ่
def deal_cards(deck):
    random.shuffle(deck)  # สับไพ่ให้สุ่ม
    dealer_hand = [deck.pop(), deck.pop()]  # ไพ่ของคนแจก 2 ใบ
    player_hand = [deck.pop(), deck.pop()]  # ไพ่ของผู้เล่น 2 ใบ
    return dealer_hand, player_hand

# ฟังก์ชั่นในการแสดงผลลัพธ์
def display_result(dealer_score, player_score):
    if player_score > dealer_score:
        return "WIN"
    elif player_score == dealer_score:
        return "DRAW"
    else:
        return "LOST"

# ฟังก์ชั่นหลักในการเล่น
def play_game():
    dealer_hand, player_hand = deal_cards(deck)
    
    # คำนวณคะแนนของคนแจกและผู้เล่น
    dealer_score = calculate_score(dealer_hand)
    player_score = calculate_score(player_hand)
    
    # แสดงไพ่และคะแนนตามรูปแบบที่คุณต้องการ
    print("*" * 5 ,"Welcome to the card game","*" *5 )
    print("-" * 36)    
    print("Dealer:")
    print(f"The first card is: {dealer_hand[0]}")
    print(f"The second card is: {dealer_hand[1]}")
    print(f"Score: {dealer_score}")
    print("-" * 36)  
    print("Player:")
    print(f"The first card is: {player_hand[0]}")
    print(f"The second card is: {player_hand[1]}")
    print(f"Score: {player_score}")
    print("=" * 36)  
    result = display_result(dealer_score, player_score)
    print(f"RESULT: {result}")
    print("=" * 36)
    
# เริ่มเกม
play_game()
