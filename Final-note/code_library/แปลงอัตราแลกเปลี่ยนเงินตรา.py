#โปรแกรมแปลงอัตราแลกเปลี่ยนเงินตราระหว่างสองสกุลเงินโดยใช้อัตราที่กำหนด
def convert_currency(amount, rate, currency_to):
    return amount * rate if currency_to.lower() == "usd" else amount / rate

# รับข้อมูลจากผู้ใช้
amount = float(input("ใส่จำนวนเงิน: "))
rate = float(input("ใส่อัตราแลกเปลี่ยน (THB/USD): "))
currency_to = input("แปลงเป็น (USD/THB): ").upper()

converted_amount = convert_currency(amount, rate, currency_to)
print(f"จำนวนเงินที่แปลงแล้ว: {converted_amount:.2f} {currency_to}")