# โปรแกรมคำนวณเงินทอนโดยไม่รวมเหรียญหรือธนบัตรที่กำหนด
# Program to calculate change excluding specific denominations
def calculate_change_exclude(total_price, payment, excluded_units):
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

    # Remove excluded denominations
    denominations = {k: v for k, v in denominations.items() if v not in excluded_units}

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
        if change > 0:  # Remaining change that can't be returned
            result.append(f"Remaining unreturnable amount: {change} Baht")
        return "\n".join(result)

while True:
    print("----------------------------------------------------------")
    excluded_units = list(map(int, input("Enter excluded units (e.g., 1,2): ").split(",")))
    total_price = int(input("The total price of products: "))
    payment = int(input("Customer payment: "))
    print("----------------------------------------------------------")

    if payment == 0:
        print("Exiting the program.")
        break

    result = calculate_change_exclude(total_price, payment, excluded_units)
    print(result)
    print("----------------------------------------------------------")