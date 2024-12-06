#เกมสุ่มโจทย์คณิตศาสตร์ให้ผู้เล่นตอบในเวลาที่กำหนด
import random
import time

def generate_math_problem():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operation = random.choice(['+', '-', '*'])
    question = f"{num1} {operation} {num2}"
    answer = eval(question)
    return question, answer

def play_math_race(rounds=5, time_limit=5):
    print("เริ่มเกมแข่งตอบคำถามคณิตศาสตร์!")
    score = 0
    for _ in range(rounds):
        question, correct_answer = generate_math_problem()
        print(f"โจทย์: {question}")
        start_time = time.time()
        try:
            user_answer = int(input("คำตอบของคุณ: "))
            if time.time() - start_time > time_limit:
                print("หมดเวลา!")
            elif user_answer == correct_answer:
                print("ถูกต้อง!")
                score += 1
            else:
                print(f"ผิด! คำตอบที่ถูกต้องคือ {correct_answer}")
        except ValueError:
            print("คำตอบไม่ถูกต้อง")
    print(f"คะแนนรวมของคุณคือ: {score}/{rounds}")

# ตัวอย่างการใช้งาน
play_math_race()