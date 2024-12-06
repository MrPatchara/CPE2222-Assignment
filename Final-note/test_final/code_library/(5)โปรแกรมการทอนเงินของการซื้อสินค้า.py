# โปรแกรมคำนวณเงินทอน
#Calculate the change and display it in a formatted way.
def calculate_change(total_price, payment): # ฟังก์ชันคำนวณเงินทอน
    denominations = { # ค่าเงินแต่ละหน่วย
        "The 500-$Baht Banknote": 500,
        "The 100-$Baht Banknote": 100,
        "The 50-$Baht Banknote": 50,
        "The 20-$Baht Banknote": 20,
        "The 10-$Baht Coin": 10,
        "The 5-$Baht Coin": 5,
        "The 2-$Baht Coin": 2,
        "The 1-$Baht Coin": 1,
    }
    change = payment - total_price # คำนวณเงินทอน

    if change < 0: # กรณีที่เงินทอนน้อยกว่า 0
        return "!!! Incorrect payment !!!"
    elif change == 0: # กรณีที่เงินทอนเท่ากับ 0
        return "Complete payment"
    else:
        result = [] # สร้างรายการเพื่อเก็บข้อมูลการคำนวณเงินทอน
        for denom, value in denominations.items(): # วนลูปเพื่อคำนวณเงินทอน
            count = change // value # คำนวณจำนวนเงินทอน
            if count > 0: # กรณีที่มีเงินทอน
                unit = "Piece(s)" if "Banknote" in denom else "Coin(s)" # หน่วยเงินทอน
                result.append(f"{denom} = {count} {unit}") # เพิ่มข้อมูลการคำนวณเงินทอน
            change %= value # คำนวณเงินทอนที่เหลือ
        return "\n".join(result) # แสดงข้อมูลการคำนวณเงินทอน

while True:
    print("----------------------------------------------------------")
    total_price = int(input("The total price of products: "))
    payment = int(input("Customer payment: "))
    print("----------------------------------------------------------")
    
    if payment == 0: # กรณีที่ป้อน 0
        print("Exiting the program.")
        break

    result = calculate_change(total_price, payment) # เรียกใช้
    print(result)
    print("----------------------------------------------------------")