# สร้างลิสต์ของค่า factorial และค่ากำลังสองของเลขแต่ละตัวในลิสต์นั้น
print('Generating Factorial series with their squared values')
n = int(input("Enter 'n' for Factorial series: "))
result = 1
factorial_list = []
squared_list = []

# Loop คำนวณ factorial และค่ากำลังสอง
for i in range(1, n+1):
    result *= i  # คำนวณ factorial
    factorial_list.append(result)  # เพิ่มค่า factorial ในลิสต์
    squared_list.append(result**2)  # เพิ่มค่ากำลังสองในลิสต์

# แสดงผล
print(f"Factorial series: {factorial_list}")
print(f"Squared values of the series: {squared_list}\n")
