import random
import time

def guessing_game_with_timer():
    random_number = random.randint(1, 99)
    attempts = 5
    low, high = 1, 99
    time_limit = 10  # กำหนดเวลาเป็น 10 วินาที

    print("***** Welcome to the Timed Guessing Game *****")

    for attempt in range(attempts):
        print(f"{'-'*21} round{attempt + 1} {'-'*21}")
        print(f"You have {time_limit} seconds to guess!")
        print(f"Enter an integer from {low} to {high} : ", end="")
        
        start_time = time.time()
        try:
            input_number = int(input())
            elapsed_time = time.time() - start_time

            if elapsed_time > time_limit:
                print("Time's up! You took too long!")
                break

            if input_number == random_number:
                print("#" * 50)
                print("   *** CONGRATULATION *** Your guess is correct  ")
                print("#" * 50)
                return
            elif input_number < random_number:
                print("Hint: Your guess is low")
                low = max(low, input_number + 1)
            else:
                print("Hint: Your guess is high")
                high = min(high, input_number - 1)
        except ValueError:
            print("Invalid input! Please enter a number.")

    print("#" * 50)
    print(f"!!!SORRY!!! The secret number is {random_number}".center(50))
    print("#" * 50)

guessing_game_with_timer()
