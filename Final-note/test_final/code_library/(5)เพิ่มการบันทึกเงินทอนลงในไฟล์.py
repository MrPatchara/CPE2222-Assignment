# โปรแกรมคำนวณเงินทอน และบันทึกข้อมูลลงไฟล์
# Program to save the change calculation to a file
def calculate_change(total_price, payment):
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

    change = payment - total_price
    if change < 0:
        return "!!! Incorrect payment !!!"
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
    payment = int(input("Customer payment: "))
    print("----------------------------------------------------------")

    if payment == 0:
        print("Exiting the program.")
        break

    result = calculate_change(total_price, payment)
    with open("change_log.txt", "a") as file:
        file.write(f"Total Price: {total_price}, Payment: {payment}\n")
        file.write(result + "\n")
        file.write("----------------------------------------------------------\n")
    print(result)
    print("Change saved to 'change_log.txt'")
    print("----------------------------------------------------------")