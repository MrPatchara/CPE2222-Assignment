# Assignment XII: 
# ฟังก์ชันสำหรับแปลงเลขอารบิกเป็นเลขโรมัน
def int_to_roman(number):
    roman_numerals = {
        1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 50: "L", 
        90: "XC", 100: "C", 400: "CD", 500: "D", 900: "CM", 1000: "M" 
    }
    # สร้างตัวแปรสำหรับเก็บเลขโรมัน
    result = "" # สร้างตัวแปรสำหรับเก็บเลขโรมัน
    for value in sorted(roman_numerals.keys(), reverse=True): # จัดเรียงค่าในพจนานุกรมจากมากไปน้อย
        while number >= value: # วนลูปเพื่อหาค่าที่มากที่สุดที่น้อยกว่าหรือเท่ากับจำนวนที่ต้องการแปลง
            result += roman_numerals[value] # เพิ่มเลขโรมันลงในผลลัพธ์
            number -= value # ลบค่าที่แปลงแล้วออกจากจำนวนที่ต้องการแปลง
    return result

# สร้างพจนานุกรมเลขอารบิก 1-39 เป็นเลขโรมัน
roman_dict = {i: int_to_roman(i) for i in range(1, 40)} # ใช้ฟังก์ชัน int_to_roman ในการแปลงเลขอารบิกเป็นเลขโรมัน

while True:
    # รับค่าอินพุตจากผู้ใช้
    number = int(input("Enter a number for Roman number conversion: "))
    
    # ตรวจสอบว่าจำนวนที่กรอกอยู่ในช่วง 1 ถึง 39 หรือไม่
    if 1 <= number <= 39:
        print(f"The roman number of {number} is {roman_dict[number]}") 
    else:
        break
