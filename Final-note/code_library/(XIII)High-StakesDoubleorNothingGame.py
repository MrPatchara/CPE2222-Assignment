import random

def high_stakes_game():
    """เกมที่คะแนนเพิ่มเป็นสองเท่าหรือสูญเสียทั้งหมด"""
    secret_number = random.randint(1, 100)
    score = 10

    print("\n***** High-Stakes Double or Nothing Game *****")
    print("Guess correctly to double your score. A wrong guess resets your score to 0.\n")

    while True:
        guess = int(input("Enter your guess: "))

        if guess == secret_number:
            score *= 2
            print(f"Correct! Your score is now {score}.")
            break
        else:
            score = 0
            print("Wrong guess! Your score is reset to 0.")
            break

    print(f"The secret number was {secret_number}. Your final score: {score}")

high_stakes_game()
