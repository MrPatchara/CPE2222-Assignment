#โปรแกรมแปลงหน่วยพื้นฐาน เช่น กิโลเมตรเป็นไมล์ หรือเซลเซียสเป็นฟาเรนไฮต์
def convert_unit(value, unit_from, unit_to):
    conversion_factors = {
        ("km", "miles"): 0.621371,
        ("miles", "km"): 1.60934,
        ("celsius", "fahrenheit"): lambda c: (c * 9/5) + 32,
        ("fahrenheit", "celsius"): lambda f: (f - 32) * 5/9
    }
    
    key = (unit_from.lower(), unit_to.lower())
    if key in conversion_factors:
        factor = conversion_factors[key]
        return factor(value) if callable(factor) else value * factor
    else:
        raise ValueError("ไม่สามารถแปลงหน่วยที่กำหนดได้")

# รับข้อมูลจากผู้ใช้
value = float(input("กรุณาใส่ค่า: "))
unit_from = input("หน่วยต้นทาง (km/miles/celsius/fahrenheit): ")
unit_to = input("หน่วยเป้าหมาย (km/miles/celsius/fahrenheit): ")

try:
    result = convert_unit(value, unit_from, unit_to)
    print(f"{value} {unit_from} = {result:.2f} {unit_to}")
except ValueError as e:
    print(e)