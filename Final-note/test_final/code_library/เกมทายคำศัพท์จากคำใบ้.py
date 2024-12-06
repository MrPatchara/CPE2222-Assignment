# โปรแกรมทายคำศัพท์จากคำใบ้
# เกมทายคำศัพท์จากคำใบ้
def play_word_guessing_game(word, hint):
    print("เริ่มเกม!")
    print(f"คำใบ้: {hint}")
    attempts = 3  # จำนวนครั้งที่ผู้เล่นสามารถเดาได้

    while attempts > 0:
        guess = input("ทายคำศัพท์: ").lower()
        if guess == word:
            print("ยินดีด้วย! คุณตอบถูกต้อง")
            return
        else:
            attempts -= 1
            print(f"ผิด! เหลือโอกาส {attempts} ครั้ง")
    
    print(f"เสียใจด้วย! คำที่ถูกต้องคือ '{word}'")

# ตัวอย่างการใช้งาน
word_to_guess = "python"
hint_for_word = "ภาษาโปรแกรมยอดนิยม"
play_word_guessing_game(word_to_guess, hint_for_word)