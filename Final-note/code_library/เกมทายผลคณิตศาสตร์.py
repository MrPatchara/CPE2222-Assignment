#เกมให้ผู้เล่นตอบคำถามคณิตศาสตร์แบบสุ่ม
import random
import operator

def generate_math_problem():
    ops = {'+': operator.add, '-': operator.sub, '*': operator.mul}
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    op = random.choice(list(ops.keys()))
    answer = ops[op](num1, num2)
    return f"{num1} {op} {num2}", answer

def play_math_game(rounds=5):
    print("เริ่มเกมทายผลคณิตศาสตร์!")
    score = 0
    for _ in range(rounds):
        problem, answer = generate_math_problem()
        print(f"คำถาม: {problem}")
        user_answer = int(input("คำตอบของคุณ: "))
        if user_answer == answer:
            print("ถูกต้อง!")
            score += 1
        else:
            print(f"ผิด! คำตอบที่ถูกต้องคือ {answer}")
    print(f"จบเกม! คุณได้คะแนน {score}/{rounds}")

# เรียกใช้งาน
play_math_game()