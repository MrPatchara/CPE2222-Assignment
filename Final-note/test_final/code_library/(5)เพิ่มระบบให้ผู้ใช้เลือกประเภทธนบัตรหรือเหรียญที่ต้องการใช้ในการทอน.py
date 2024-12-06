# โปรแกรมคำนวณเงินทอน โดยรับค่าราคาสินค้า และจำนวนเงินที่ลูกค้าจ่าย และรายการเหรียญที่ใช้ในการทอนเงิน
# Program to calculate change with user-specified denominations
def calculate_change_custom(total_price, payment, allowed_denominations):
    change = payment - total_price
    if change < 0:
        return "!!! Incorrect payment !!!"
    elif change == 0:
        return "Complete payment"
    else:
        result = []
        for denom, value in allowed_denominations.items():
            count = change // value
            if count > 0:
                result.append(f"{denom} = {count} Piece(s)")
            change %= value
        return "\n".join(result)

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

while True:
    print("----------------------------------------------------------")
    allowed = input("Enter denominations to use (e.g., 500,100,50): ").split(",")
    allowed_denominations = {k: v for k, v in denominations.items() if str(v) in allowed}
    total_price = int(input("The total price of products: "))
    payment = int(input("Customer payment: "))
    print("----------------------------------------------------------")

    if payment == 0:
        print("Exiting the program.")
        break

    result = calculate_change_custom(total_price, payment, allowed_denominations)
    print(result)
    print("----------------------------------------------------------")