# โปรแกรมคำนวณ Factorial ของเลขคู่และเลขคี่
# สร้างลิสต์ Factorial ที่คำนวณเฉพาะเลขคี่
print('Generating Odd Factorial series')
n = int(input("Enter 'n' for Odd Factorial series: "))
result = 1
odd_factorial_list = []

# คำนวณ Factorial เฉพาะเลขคี่
for i in range(1, n+1):
    if i % 2 != 0:  # เช็คว่าเลขเป็นคี่
        result *= i
        odd_factorial_list.append(result)

# แสดงผล
print(f"Odd Factorial series: {odd_factorial_list}\n")
