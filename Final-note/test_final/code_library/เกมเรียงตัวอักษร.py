# โปรแกรมเกมสับเปลี่ยนคำ (Word Scramble Game)
#เกมให้ผู้เล่นเรียงตัวอักษรที่ถูกสับเปลี่ยนให้กลับเป็นคำที่ถูกต้อง
import random

def scramble_word(word):
    word = list(word)
    random.shuffle(word)
    return ''.join(word)

def play_word_scramble_game(word):
    scrambled = scramble_word(word)
    print(f"คำที่สับเปลี่ยน: {scrambled}")
    attempts = 3
    while attempts > 0:
        guess = input("ลองเรียงตัวอักษร: ")
        if guess == word:
            print("ยินดีด้วย! คุณเรียงถูกต้อง")
            return
        else:
            attempts -= 1
            print(f"ผิด! เหลือโอกาส {attempts} ครั้ง")
    print(f"เสียใจด้วย! คำที่ถูกต้องคือ '{word}'")

# ตัวอย่างการใช้งาน
play_word_scramble_game("python")