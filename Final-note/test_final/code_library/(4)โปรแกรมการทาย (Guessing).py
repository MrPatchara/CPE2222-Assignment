# โปรแกรมทายเลข 4 หลัก โดยมีเงื่อนไขดังนี้
# 1. หากผู้เล่นทายเลขถูกต้อง โปรแกรมจะแสดงข้อความ "Congratulations" พร้อมกับจำนวนครั้งที่ทายถูกต้อง
# 2. หากผู้เล่นต้องการออกจากโปรแกรม สามารถกด 0 เพื่อออกจากโปรแกรมได้
# 3. หากผู้เล่นป้อนตัวเลขที่ไม่ใช่ 4 หลัก หรือป้อนตัวเลขที่มีตัวเลขซ้ำกัน โปรแกรมจะแสดงข้อความ "Invalid input"
# 4. หากผู้เล่นทายเลขไม่ถูกต้อง โปรแกรมจะแสดงจำนวน
import random

def generate_secret_number():
    """Generate a 4-digit secret number with unique digits."""
    return random.sample(range(10), 4)

def calculate_hint(secret, guess):
    """Calculate MEN and WOMEN based on the guess."""
    men = sum(s == g for s, g in zip(secret, guess))
    women = sum(g in secret for g in guess) - men
    return men, women

# Main program
print("------ Welcome to MEN and WOMEN number guessing game ------")
print("[To exit the program, press 0]")
print("----------------------------------------------------------")

# Generate the secret number
secret_number = generate_secret_number()

attempts = 0

while True:
    user_input = input("Enter 4-digits number: ")

    if user_input == "0":
        print(f"Secret Number was: {''.join(map(str, secret_number))}")
        print("Exiting the program.")
        break

    if len(user_input) != 4 or not user_input.isdigit():
        print("Invalid input. Please enter a 4-digit number.")
        continue

    guess = list(map(int, user_input))
    if len(set(guess)) != 4:
        print("Digits must be unique. Try again.")
        continue

    attempts += 1
    men, women = calculate_hint(secret_number, guess)

    print(f"Hint: MEN = {men} and WOMEN = {women}")

    if men == 4:
        print(f"*** Congratulations *** Your guess is correct, after {attempts} times")
        print(f"Secret Number was: {''.join(map(str, secret_number))}")
        break