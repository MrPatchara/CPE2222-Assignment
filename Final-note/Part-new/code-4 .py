# โปรแกรมในการรับค่าตัวเลขที่มีค่าตั้งแต่ 0 จนถึง 5,000 แล้วเปลี่ยนตัวเลขนั้นเป็นข้อความภาษาอังกฤษ โดยหากรับค่านอกเหนือจากตัวเลขที่มีค่าตั้งแต่ 0 จนถึง 5,000 ให้โปรแกรมหยุดการทำงาน

def number_to_words(num):
    if num == 0:
        return "Zero"
    
    ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    thousands = ["", "Thousand"]

    # แปลงตัวเลขเป็นข้อความ
    words = []
    
    # แปลงส่วนพัน 
    if num >= 1000:
        words.append(ones[num // 1000] + " Thousand")
        num %= 1000
    
    # แปลงส่วนร้อย 
    if num >= 100:
        words.append(ones[num // 100] + " Hundred")
        num %= 100
    
    # แปลงส่วนสิบและหน่วย 
    if num >= 20:
        words.append(tens[num // 10])
        num %= 10

    # แปลงส่วนสิบและหน่วย (สำหรับเลข 10-19)
    if 10 <= num < 20:
        words.append(teens[num - 10])
        num = 0
    
    # แปลงส่วนหน่วย
    if num > 0:
        words.append(ones[num])

    # รวมข้อความทั้งหมด
    return ' '.join(words).strip()

def main():
    while True:
        try:
            # รับค่าตัวเลขจากผู้ใช้
            num = int(input("Enter a number for word conversion (between 0 and 5000): "))
            
            # ตรวจสอบว่าเลขที่กรอกอยู่ในช่วง 0-5000 หรือไม่
            if 0 <= num <= 5000:
                print(number_to_words(num))  # แปลงเลขเป็นข้อความภาษาอังกฤษ
            else:
                print("Out of range")
                break  # หยุดการทำงานเมื่อกรอกเลขนอกช่วง
        except ValueError:
            print("only numbers are allowed")  

# เรียกใช้ฟังก์ชัน
main()
