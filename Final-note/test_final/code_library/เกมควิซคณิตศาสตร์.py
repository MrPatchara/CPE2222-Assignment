# โปรแกรมสุ่มโจทย์คณิตศาสตร์ให้ผู้เล่นตอบ
#เกมสุ่มโจทย์คณิตศาสตร์ให้ผู้เล่นตอบ
import random

def generate_question():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operation = random.choice(['+', '-', '*'])
    question = f"{num1} {operation} {num2}"
    answer = eval(question)
    return question, answer

def play_math_quiz(rounds=5):
    print("เริ่มเกมควิซคณิตศาสตร์!")
    score = 0
    for _ in range(rounds):
        question, correct_answer = generate_question()
        print(f"โจทย์: {question}")
        user_answer = int(input("คำตอบของคุณ: "))
        if user_answer == correct_answer:
            print("ถูกต้อง!")
            score += 1
        else:
            print(f"ผิด! คำตอบที่ถูกต้องคือ {correct_answer}")
    print(f"คะแนนรวมของคุณคือ: {score}/{rounds}")

# ตัวอย่างการใช้งาน
play_math_quiz()