#โปรแกรมคำนวณแฟกทอเรียลของตัวเลขที่ป้อน
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# รับข้อมูลจากผู้ใช้
number = int(input("กรุณาใส่ตัวเลขที่ต้องการคำนวณแฟกทอเรียล: "))
if number < 0:
    print("ไม่สามารถคำนวณแฟกทอเรียลของเลขลบได้")
else:
    result = factorial(number)
    print(f"{number}! = {result}")