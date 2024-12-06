# โปรแกรมคำนวณเงินทอน แต่ใช้แบงค์เท่านั้น
# Program to calculate change with notes only
def calculate_change_no_coins(total_price, payment):
    denominations = {
        "The 500-$Baht Banknote": 500,
        "The 100-$Baht Banknote": 100,
        "The 50-$Baht Banknote": 50,
        "The 20-$Baht Banknote": 20,
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
                result.append(f"{denom} = {count} Note(s)")
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

    result = calculate_change_no_coins(total_price, payment)
    print(result)
    print("----------------------------------------------------------")