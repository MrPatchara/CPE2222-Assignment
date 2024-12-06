#โปรแกรมแปลงอุณหภูมิระหว่างเซลเซียส ฟาเรนไฮต์ และเคลวิน
def convert_temperature(value, from_unit, to_unit):
    if from_unit == "C":
        if to_unit == "F":
            return (value * 9/5) + 32
        elif to_unit == "K":
            return value + 273.15
    elif from_unit == "F":
        if to_unit == "C":
            return (value - 32) * 5/9
        elif to_unit == "K":
            return (value - 32) * 5/9 + 273.15
    elif from_unit == "K":
        if to_unit == "C":
            return value - 273.15
        elif to_unit == "F":
            return (value - 273.15) * 9/5 + 32
    return value

# รับข้อมูลจากผู้ใช้
value = float(input("กรุณาใส่อุณหภูมิ: "))
from_unit = input("หน่วยต้นทาง (C/F/K): ").upper()
to_unit = input("หน่วยเป้าหมาย (C/F/K): ").upper()

converted = convert_temperature(value, from_unit, to_unit)
print(f"{value} {from_unit} = {converted:.2f} {to_unit}")