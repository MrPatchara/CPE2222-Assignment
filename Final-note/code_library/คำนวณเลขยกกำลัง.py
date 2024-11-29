#โปรแกรมคำนวณค่าผลลัพธ์ของเลขฐานและเลขยกกำลังที่ป้อน
def calculate_power(base, exponent):
    return base ** exponent

# รับค่าจากผู้ใช้
base = float(input("กรุณาใส่เลขฐาน: "))
exponent = int(input("กรุณาใส่เลขยกกำลัง: "))

result = calculate_power(base, exponent)
print(f"{base} ยกกำลัง {exponent} = {result:.2f}")