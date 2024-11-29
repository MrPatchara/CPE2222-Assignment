import random

def dynamic_guessing_game():
    low, high = 1, 99
    attempts = 5

    print("***** Welcome to the Dynamic Guessing Game *****")
    random_number = random.randint(low, high)  # สุ่มตัวเลขเริ่มต้น

    for attempt in range(attempts):
        print(f"{'-'*21} round{attempt + 1} {'-'*21}")
        print(f"Enter an integer from {low} to {high} : ", end="")
        
        input_number = int(input())
        
        if input_number == random_number:
            print("#" * 50)
            print("   *** CONGRATULATION *** Your guess is correct  ")
            print("#" * 50)
            return
        else:
            print("Wrong guess! A new secret number has been generated.")
            random_number = random.randint(low, high)  # สุ่มตัวเลขใหม่ทุกครั้ง
            if input_number < random_number:
                print("Hint: Your guess was too low.")
            else:
                print("Hint: Your guess was too high.")

    print("#" * 50)
    print("You have run out of attempts!")
    print("#" * 50)

dynamic_guessing_game()
