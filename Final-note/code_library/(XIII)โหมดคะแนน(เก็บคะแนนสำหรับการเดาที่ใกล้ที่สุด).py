import random

def scoring_guessing_game():
    random_number = random.randint(1, 99)
    attempts = 5
    low, high = 1, 99
    score = 100  # เริ่มต้นด้วยคะแนนเต็ม 100

    print("***** Welcome to the Scoring Guessing Game *****")

    for attempt in range(attempts):
        print(f"{'-'*21} round{attempt + 1} {'-'*21}")
        print(f"Enter an integer from {low} to {high} : ", end="")
        input_number = int(input())
        
        if input_number == random_number:
            print("#" * 50)
            print("   *** CONGRATURATION *** Your guess is correct  ")
            print(f"Your final score is {score}")
            print("#" * 50)
            return
        else:
            diff = abs(input_number - random_number)
            if diff <= 10:
                score -= 5  # หัก 5 คะแนนถ้าเดาใกล้
                print("Close! But not quite.")
            else:
                score -= 10  # หัก 10 คะแนนถ้าเดาห่าง
                print("Not even close!")

            if input_number < random_number:
                print("Hint: Your guess is low")
                low = max(low, input_number + 1)
            else:
                print("Hint: Your guess is high")
                high = min(high, input_number - 1)

    print("#" * 50)
    print(f"!!!SORRY!!! The secret number is {random_number}".center(50))
    print(f"Your final score is {score}".center(50))
    print("#" * 50)

scoring_guessing_game()
