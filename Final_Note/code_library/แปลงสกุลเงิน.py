#โปรแกรมแปลงสกุลเงินระหว่าง USD และ THB โดยใช้อัตราแลกเปลี่ยนที่กำหนด
def convert_currency(amount, rate, to_currency):
    if to_currency == "USD":
        return amount / rate
    elif to_currency == "THB":
        return amount * rate
    else:
        raise ValueError("สกุลเงินไม่รองรับ")

# อัตราแลกเปลี่ยนปัจจุบัน (สมมติ)
exchange_rate = 33.5

# รับข้อมูลจากผู้ใช้
amount = float(input("กรุณาใส่จำนวนเงิน: "))
currency = input("แปลงเป็นสกุลเงิน (USD/THB): ").upper()

try:
    converted = convert_currency(amount, exchange_rate, currency)
    print(f"จำนวนเงินที่แปลงคือ: {converted:.2f} {currency}")
except ValueError as e:
    print(e)