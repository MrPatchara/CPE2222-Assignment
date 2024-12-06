# โปรแกรมคำนวณเงินทอนเมื่อมีหลายคนจ่ายเงินร่วมกัน
# Program to calculate change when multiple people pay together
def calculate_change(total_price, payments):
    denominations = {
        "The 500-$Baht Banknote": 500,
        "The 100-$Baht Banknote": 100,
        "The 50-$Baht Banknote": 50,
        "The 20-$Baht Banknote": 20,
        "The 10-$Baht Coin": 10,
        "The 5-$Baht Coin": 5,
        "The 2-$Baht Coin": 2,
        "The 1-$Baht Coin": 1,
    }

    total_payment = sum(payments)
    change = total_payment - total_price

    if change < 0:
        return "!!! Insufficient payment !!!"
    elif change == 0:
        return "Complete payment"
    else:
        result = []
        for denom, value in denominations.items():
            count = change // value
            if count > 0:
                result.append(f"{denom} = {count} Piece(s)")
            change %= value
        return "\n".join(result)

while True:
    print("----------------------------------------------------------")
    total_price = int(input("The total price of products: "))
    num_people = int(input("Enter the number of people paying: "))
    payments = [int(input(f"Payment from person {i + 1}: ")) for i in range(num_people)]
    print("----------------------------------------------------------")

    if sum(payments) == 0:
        print("Exiting the program.")
        break

    result = calculate_change(total_price, payments)
    print(result)
    print("----------------------------------------------------------")