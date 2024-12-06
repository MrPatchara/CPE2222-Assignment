# โปรแกรมเกม Hangman ที่ให้ผู้เล่นทายคำศัพท์ทีละตัวอักษรจนกว่าจะครบหรือพลาดเกินจำนวนครั้งที่กำหนด
#เกมให้ผู้เล่นทายคำศัพท์ทีละตัวอักษรจนกว่าจะครบหรือพลาดเกินจำนวนครั้งที่กำหนด
def play_hangman(word):
    guessed = set()
    attempts = len(word) + 3
    current_state = ["_" for _ in word]

    print("เริ่มเกม Hangman!")
    while attempts > 0:
        print(" ".join(current_state))
        guess = input("ใส่ตัวอักษรที่ต้องการทาย: ").lower()
        
        if guess in guessed:
            print("คุณทายตัวอักษรนี้ไปแล้ว")
        elif guess in word:
            print("ถูกต้อง!")
            guessed.add(guess)
            for i, char in enumerate(word):
                if char == guess:
                    current_state[i] = guess
            if "_" not in current_state:
                print(f"ยินดีด้วย! คุณทายคำว่า '{word}' สำเร็จ")
                return
        else:
            print("ผิด!")
            guessed.add(guess)
            attempts -= 1
        
        print(f"เหลือโอกาสทายอีก {attempts} ครั้ง")
    
    print(f"เสียใจด้วย! คำที่ถูกต้องคือ '{word}'")

# ตัวอย่างการใช้งาน
play_hangman("python")