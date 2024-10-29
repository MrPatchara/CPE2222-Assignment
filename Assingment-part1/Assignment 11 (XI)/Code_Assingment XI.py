def factorial_list(n): # สร้างฟังก์ชัน factorial_list ที่รับค่า n เพื่อหาค่า factorial ของตัวเลขที่รับมา
    factorials = [] # สร้าง list เพื่อเก็บค่า factorial
    factorial = 1 # กำหนดค่า factorial เริ่มต้น
    for i in range(1, n + 1): # วนลูปเพื่อหาค่า factorial ของตัวเลขที่รับมา
        factorial *= i # คูณตัวเลขก่อนหน้าเพื่อหาค่า factorial ของตัวเลขปัจจุบัน 
        factorials.append(factorial) # เพิ่มค่า factorial ลงใน list
    return factorials 

# รับค่าจำนวนเต็มจากผู้ใช้
print("Making a list of Factorial series of n")
n = int(input("Enter 'n' of Factorial number: "))
factorials = factorial_list(n)
print("A list of Factorial series of", n, "is", factorials)
