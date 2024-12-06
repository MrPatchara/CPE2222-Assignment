# โปรแกรมตรวจสอบว่าเลขที่รับมาเป็นจำนวนเฉพาะหรือไม่
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

# รับค่าจากผู้ใช้
num = int(input("ใส่ตัวเลขที่ต้องการตรวจสอบ: "))
if is_prime(num):
    print(f"{num} เป็นจำนวนเฉพาะ")
else:
    print(f"{num} ไม่ใช่จำนวนเฉพาะ")
