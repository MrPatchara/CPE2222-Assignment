# โปรแกรมทายตัวเลขที่ผู้เล่นกำหนด
# โดยเครื่องจะทายตัวเลขที่ผู้เล่นกำหนด โดยการใช้วิธีการทายแบบทวิภาค
def reverse_guessing_game():
    """เครื่องพยายามทายตัวเลขที่ผู้เล่นกำหนด"""
    print("\nThink of a number between 1 and 100, and I will try to guess it.")
    low, high = 1, 100

    while low <= high: # วนลูปจนกว่าช่วงจะยังไม่เสร็จสิ้น
        guess = (low + high) // 2 # ทายตัวเลขตรงกลางของช่วง
        print(f"My guess is {guess}.")
        response = input("Is it correct (c), too low (l), or too high (h)? ").lower()

        if response == 'c': # ถ้าทายถูก
            print("Yay! I guessed it!") # แสดงข้อความว่าทายถูก
            return
        elif response == 'l': # ถ้าทายต่ำเกิน
            low = guess + 1 # ปรับค่าต่ำสุด
        elif response == 'h': # ถ้าทายสูงเกิน
            high = guess - 1 # ปรับค่าสูงสุด
        else:
            print("Invalid response. Please enter 'c', 'l', or 'h'.")

    print("Something went wrong. Are you sure you thought of a number?")

reverse_guessing_game()
