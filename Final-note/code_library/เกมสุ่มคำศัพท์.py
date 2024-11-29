import random

def play_word_guessing_game(words):
    # สุ่มเลือกคำจากรายการ
    word_to_guess = random.choice(words).lower()
    guessed_word = ['_' for _ in word_to_guess]
    attempts = 6  # จำนวนโอกาสที่ให้เดา

    print("เริ่มเกมเดาคำศัพท์! คุณมีโอกาส 6 ครั้ง")
    while attempts > 0:
        print("คำปัจจุบัน:", ' '.join(guessed_word))
        guess = input("ใส่ตัวอักษร: ").lower()

        if guess in word_to_guess:
            for i, char in enumerate(word_to_guess):
                if char == guess:
                    guessed_word[i] = guess
            if '_' not in guessed_word:
                print(f"ยินดีด้วย! คุณเดาคำว่า '{word_to_guess}' ได้สำเร็จ")
                break
        else:
            attempts -= 1
            print(f"ผิด! เหลือโอกาส {attempts} ครั้ง")
        
        if attempts == 0:
            print(f"เกมจบ! คำที่ต้องเดาคือ '{word_to_guess}'")

# เรียกใช้งาน
word_list = ["Python", "Programming", "Game", "Learning", "AI"]
play_word_guessing_game(word_list)
