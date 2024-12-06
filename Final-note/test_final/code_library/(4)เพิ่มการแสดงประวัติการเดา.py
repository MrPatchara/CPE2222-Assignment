# เกม MEN and WOMEN โดยเพิ่มประวัติการเดา
import random

def generate_secret_number():
    """Generate a 4-digit secret number with unique digits."""
    return random.sample(range(10), 4)

def calculate_hint(secret, guess):
    """Calculate MEN and WOMEN based on the guess."""
    men = sum(s == g for s, g in zip(secret, guess))
    women = sum(g in secret for g in guess) - men
    return men, women

print("------ Welcome to MEN and WOMEN number guessing game ------")
print("[To exit the program, press 0]")
print("----------------------------------------------------------")

secret_number = generate_secret_number()
attempts = 0
history = []  # เก็บประวัติการเดา

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
    history.append((guess, men, women))  # เก็บข้อมูลการเดา

    print(f"Hint: MEN = {men} and WOMEN = {women}")

    if men == 4:
        print(f"*** Congratulations *** Your guess is correct, after {attempts} attempts")
        print(f"Secret Number was: {''.join(map(str, secret_number))}")
        break

    # แสดงประวัติการเดา
    print("\nYour Guess History:")
    for idx, (g, m, w) in enumerate(history):
        print(f"{idx + 1}: {''.join(map(str, g))} -> MEN: {m}, WOMEN: {w}")
    print()