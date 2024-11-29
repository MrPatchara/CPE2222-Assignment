import random

def guessing_game():
    random_number = random.randint(1, 99)
    attempts = 5
    low, high = 1, 99

    print("***** Welcome to the game of guessing number *****")

    for attempt in range(attempts):
        print(f"{'-'*21} round{attempt + 1} {'-'*21}")
        print(f"Enter an integer from {low} to {high} : ", end="")

        input_number = int(input())

        if input_number == random_number:
            print("#" * 50)
            print("   *** CONGRATURATION *** Your guess is correct  ")
            print("#" * 50)
            return
        
        elif input_number < random_number:
            print("Hint: Your guess is low")
            low = max(low, input_number + 1)
        else:
            print("Hint: Your guess is high")
            high = min(high, input_number - 1)

    print("#" * 50)
    print(f"!!!SORRY!!! The secret number is {random_number}".center(50))
    print("#" * 50)

guessing_game()
