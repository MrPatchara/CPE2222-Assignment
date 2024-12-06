# โปรแกรมคำนวณเงินทอนด้วยหน่วยเงินที่กำหนดเอง
# Program to calculate change with custom currency units
def calculate_change(total_price, payment, denominations):
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
    custom_denominations = input("Enter custom denominations (e.g., '100:100,50:50,20:20'): ")
    denominations = {k: int(v) for k, v in (pair.split(":") for pair in custom_denominations.split(","))}
    total_price = int(input("The total price of products: "))
    payment = int(input("Customer payment: "))
    print("----------------------------------------------------------")

    if payment == 0:
        print("Exiting the program.")
        break

    result = calculate_change(total_price, payment, denominations)
    print(result)
    print("----------------------------------------------------------")