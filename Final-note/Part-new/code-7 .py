# 7.จงเขียนโปรแกรมในการรับค่าตัวเลขและนับจำนวนหลัก (Digit) ของตัวเลขนั้น โดยค่าที่รับได้มานั้นสามารถเป็นได้ทั้งจำนวนเต็ม (Integer) และเลขทศนิยม (Decimal number) การนับจำนวนหลักให้นับทั้งในส่วนที่เป็นจำนวนเต็มและเลขทศนิยม ดังแสดงในตัวอย่างต่อไปนี้
# ฟังก์ชันสำหรับการนับจำนวนหลัก

def count_digits(number):
    # เปลี่ยนตัวเลขเป็นสตริง
    num_str = str(number)
    
    # ถ้ามีเครื่องหมายลบ ให้ตัดเครื่องหมายลบออก
    if num_str.startswith('-'):
        num_str = num_str[1:]
    
    # ถ้ามีจุดทศนิยมให้แยกส่วนจำนวนเต็มและทศนิยม
    if '.' in num_str:
        integer_part, decimal_part = num_str.split('.')
        # ลบศูนย์นำหน้าในส่วนจำนวนเต็ม
        integer_part = integer_part.lstrip('0') if integer_part != '' else '0'
        # ลบศูนย์หลังจุดทศนิยม
        decimal_part = decimal_part.rstrip('0')
        
        integer_digits = len(integer_part)
        decimal_digits = len(decimal_part)
    else:
        # ถ้าไม่มีจุดทศนิยมให้ทำการลบศูนย์นำหน้าในส่วนจำนวนเต็ม
        integer_part = num_str.lstrip('0') if num_str != '' else '0'
        integer_digits = len(integer_part)
        decimal_digits = 0  # ไม่มีทศนิยม
    
    return integer_digits, decimal_digits

# รับค่าตัวเลขจากผู้ใช้
number = input("Enter a number (can be either an integer or a decimal number): ")

# เรียกฟังก์ชันเพื่อนับจำนวนหลัก
integer_digits, decimal_digits = count_digits(number)

# แสดงผล
print(f"Integer digit: {integer_digits}")
print(f"Decimal digit: {decimal_digits}\n")
