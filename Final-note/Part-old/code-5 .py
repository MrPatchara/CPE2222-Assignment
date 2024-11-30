#5.จง เขียนโปรแกรมการทอนเงินของการซื้อสินค้า โดย มีหลักการทำงานดังต่อไปนี้

def calculate_change(total_price, payment):
    # ตรวจสอบว่าการชำระเงินถูกต้องหรือไม่
    if payment < total_price:
        print("!!! Incorrect payment !!!")
        return
    elif payment == total_price:
        print("Complete payment")
        return

    # คำนวณเงินทอน
    change = payment - total_price
    
    # ข้อมูลธนบัตรและเหรียญที่ใช้ทอน
    denominations = [
        (500, "The 500-$Baht Banknote"),
        (100, "The 100-$Baht Banknote"),
        (50, "The 50-$Baht Banknote"),
        (20, "The 20-$Baht Banknote"),
        (10, "The 10-$Baht Coin"),
        (5, "The 5-$Baht Coin"),
        (2, "The 2-$Baht Coin"),
        (1, "The 1-$Baht Coin")
    ]
    
    print(f"Money Return : {change} $Baht")
    print("="*35)
    
    # การคำนวณและแสดงผลธนบัตรและเหรียญที่ใช้ทอน
    print("List of money return")
    for value, name in denominations:
        count = change // value  # หาจำนวนธนบัตรหรือเหรียญที่ใช้
        if count > 0:
            # แยกแสดงผลสำหรับธนบัตรและเหรียญ
            if value >= 20:
                print(f"{name} = {count} Piece(s)")  # สำหรับธนบัตร
            else:
                print(f"{name} = {count} Coin(s)")  # สำหรับเหรียญ
            change -= count * value  # ลดจำนวนเงินที่ยังต้องทอน

# รับข้อมูลจากผู้ใช้
try:
    print("-"*35)
    total_price = int(input("The total price of product: "))
    payment = int(input("Customer payment: "))
    print("-"*35)
    calculate_change(total_price, payment)
    print("-"*35)
except ValueError:
    print("!!! Incorrect payment !!!")
