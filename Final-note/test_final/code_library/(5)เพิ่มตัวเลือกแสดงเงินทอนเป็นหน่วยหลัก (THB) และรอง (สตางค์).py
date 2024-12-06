# โปรแกรมคำนวณเงินทอนด้วยหน่วยสตางค์ไทย
# Program to calculate change with Thai Satang units
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
        "The 50-Satang Coin": 0.5,
        "The 25-Satang Coin": 0.25,
    }

    change = payment - total_price
    if change < 0:
        return "!!! Incorrect payment !!!"
    elif change == 0:
        return "Complete payment"
    else:
        result = []
        for denom, value in denominations.items():
            count = int(change // value)
            if count > 0:
                unit = "Piece(s)"
                result.append(f"{denom} = {count} {unit}")
            change = round(change % value, 2)
        return "\n".join(result)

while True:
    print("----------------------------------------------------------")
    total_price = float(input("The total price of products (THB): "))
    payment = float(input("Customer payment (THB): "))
    print("----------------------------------------------------------")

    if payment == 0:
        print("Exiting the program.")
        break

    result = calculate_change(total_price, payment)
    print(result)
    print("----------------------------------------------------------")