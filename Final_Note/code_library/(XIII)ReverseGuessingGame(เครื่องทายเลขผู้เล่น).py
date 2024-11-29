def reverse_guessing_game():
    """เครื่องพยายามทายตัวเลขที่ผู้เล่นกำหนด"""
    print("\nThink of a number between 1 and 100, and I will try to guess it.")
    low, high = 1, 100

    while low <= high:
        guess = (low + high) // 2
        print(f"My guess is {guess}.")
        response = input("Is it correct (c), too low (l), or too high (h)? ").lower()

        if response == 'c':
            print("Yay! I guessed it!")
            return
        elif response == 'l':
            low = guess + 1
        elif response == 'h':
            high = guess - 1
        else:
            print("Invalid response. Please enter 'c', 'l', or 'h'.")

    print("Something went wrong. Are you sure you thought of a number?")

reverse_guessing_game()
