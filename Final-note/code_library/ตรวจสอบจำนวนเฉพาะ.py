#โปรแกรมตรวจสอบว่าตัวเลขที่ป้อนเป็นจำนวนเฉพาะหรือไม่
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

# รับข้อมูลจากผู้ใช้
number = int(input("กรุณาใส่ตัวเลขที่ต้องการตรวจสอบ: "))
if is_prime(number):
    print(f"{number} เป็นจำนวนเฉพาะ")
else:
    print(f"{number} ไม่ใช่จำนวนเฉพาะ")