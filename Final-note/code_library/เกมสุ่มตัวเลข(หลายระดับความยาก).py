import random

def play_guessing_game(level):
    if level == 'ง่าย':
        number = random.randint(1, 10)
        attempts = 5
    elif level == 'ปานกลาง':
        number = random.randint(1, 50)
        attempts = 7
    elif level == 'ยาก':
        number = random.randint(1, 100)
        attempts = 10
    else:
        print("ระดับความยากไม่ถูกต้อง")
        return

    print(f"เริ่มเกม! คุณมี {attempts} ครั้งในการทายตัวเลข")
    while attempts > 0:
        guess = int(input("ทายตัวเลขของคุณ: "))
        if guess < number:
            print("ตัวเลขต่ำเกินไป!")
        elif guess > number:
            print("ตัวเลขสูงเกินไป!")
        else:
            print(f"ยินดีด้วย! คุณทายถูกต้อง ตัวเลขคือ {number}")
            return
        attempts -= 1
        print(f"เหลือโอกาส {attempts} ครั้ง")
    
    print(f"เสียใจด้วย คุณแพ้! ตัวเลขคือ {number}")

# เลือกระดับความยากและเล่นเกม
difficulty = input("เลือกระดับความยาก (ง่าย/ปานกลาง/ยาก): ")
play_guessing_game(difficulty)