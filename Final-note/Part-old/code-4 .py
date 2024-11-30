#4.จงเขียนโปรแกรมการ ทาย (Guessing) ตัว เลข 0 – 9 จำนวน 4 ตำแหน่ง โดย ตัวเลข แต่ละตำแหน่งมี ค่า ไม่ ซ้ำกัน ใน การ ทาย แต่ละครั้งโปรแกรมจะให้คำใบ้ ( Hint) ว่า มีจำนวนของ ผู้ชาย (Men) และ ผู้หญิง (Women)

print("\n")
print("-"*5,"Welcome to MEN and WOMEN number guessing game", "-"*5)
print("[To exit the program, press 0]")
print("-"*57)

import random
def generate_secret_number():
    # สุ่มตัวเลข 4 หลักที่ไม่ซ้ำกัน
    digits = random.sample(range(10), 4)
    return ''.join(map(str, digits))

def give_hint(guess, secret):
    men = 0
    women = 0
    for i in range(4):
        if guess[i] == secret[i]:
            men += 1
        elif guess[i] in secret:
            women += 1
    return men, women

def main():
    secret_number = generate_secret_number()
    attempts = 0

    print("Secret number : ", secret_number)
    print("="*57)

    while True:
        guess = input("Enter 4-digits number : ")
        
        if guess == '0':
            print("Exiting...")
            break
        
        if len(guess) != 4 or not guess.isdigit() or len(set(guess)) != 4:
            print("Invalid input. Please enter 4 unique digits.")
            continue

        attempts += 1
        men, women = give_hint(guess, secret_number)

        print(f"Hint : MEN = {men} and WOMEN = {women}")
        
        if men == 4:
            print(f"*** Congratuation *** your guess is correct, after {attempts} times\n")
            break

if __name__ == "__main__":
    main()
