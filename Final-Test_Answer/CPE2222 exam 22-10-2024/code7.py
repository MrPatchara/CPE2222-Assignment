def count_digits(number):
    # เปลี่ยนตัวเลขเป็นสตริง
    num_str = str(number)
    # ถ้ามีเครื่องหมายลบ 
    if num_str.startswith('-'):
        num_str = num_str[1:]
    # ถ้ามีจุดทศนิยม
    if '.' in num_str:
        integer_part, decimal_part = num_str.split('.')
        # ลบศูนย์นำหน้าจํานวนเต็ม
        integer_part = integer_part.lstrip('0') if integer_part != '' else '0'
        # ลบศูนย์หลังจุด
        decimal_part = decimal_part.rstrip('0')     
        integer_digits = len(integer_part)
        decimal_digits = len(decimal_part)
    else:
        integer_part = num_str.lstrip('0') if num_str != '' else '0'
        integer_digits = len(integer_part)
        decimal_digits = 0  
    return integer_digits, decimal_digits

number = input("Enter a number (can be either an integer or a decimal number): ")

integer_digits, decimal_digits = count_digits(number)

print(f"Integer digit: {integer_digits}")
print(f"Decimal digit: {decimal_digits}\n")
