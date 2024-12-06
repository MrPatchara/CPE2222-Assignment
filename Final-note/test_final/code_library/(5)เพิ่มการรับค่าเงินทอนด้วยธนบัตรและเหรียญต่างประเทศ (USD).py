# โปรแกรมคำนวณเงินทอน และแสดงจำนวนแบงค์และเหรียญที่ต้องทอน โดยมีตัวเลือกในการเลือกสกุลเงิน USD หรือ THB
# Program to calculate change with options for USD denominations
def calculate_change(total_price, payment, currency="THB"):
    denominations = {
        "THB": {
            "The 500-$Baht Banknote": 500,
            "The 100-$Baht Banknote": 100,
            "The 50-$Baht Banknote": 50,
            "The 20-$Baht Banknote": 20,
            "The 10-$Baht Coin": 10,
            "The 5-$Baht Coin": 5,
            "The 2-$Baht Coin": 2,
            "The 1-$Baht Coin": 1,
        },
        "USD": {
            "The 100-$Bill": 100,
            "The 50-$Bill": 50,
            "The 20-$Bill": 20,
            "The 10-$Bill": 10,
            "The 5-$Bill": 5,
            "The 1-$Bill": 1,
            "The 25c-Coin": 0.25,
            "The 10c-Coin": 0.10,
            "The 5c-Coin": 0.05,
            "The 1c-Coin": 0.01,
        },
    }

    if currency not in denominations:
        return "Unsupported currency!"

    change = payment - total_price
    if change < 0:
        return "!!! Incorrect payment !!!"
    elif change == 0:
        return "Complete payment"
    else:
        result = []
        for denom, value in denominations[currency].items():
            count = int(change // value)
            if count > 0:
                unit = "Piece(s)" if "Coin" in denom or "c" in denom else "Note(s)"
                result.append(f"{denom} = {count} {unit}")
            change %= value
        return "\n".join(result)

while True:
    print("----------------------------------------------------------")
    currency = input("Enter currency (THB/USD): ").strip().upper()
    total_price = float(input("The total price of products: "))
    payment = float(input("Customer payment: "))
    print("----------------------------------------------------------")
    
    if payment == 0:
        print("Exiting the program.")
        break

    result = calculate_change(total_price, payment, currency)
    print(result)
    print("----------------------------------------------------------")