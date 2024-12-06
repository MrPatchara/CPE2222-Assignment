# โปรแกรมสร้างลิสต์ Factorial และ Fibonacci พร้อมกัน
# สร้างลิสต์ Factorial และ Fibonacci พร้อมกัน
print('Generating Factorial and Fibonacci series')
n = int(input("Enter 'n' for series: "))
result = 1
factorial_list = []
fibonacci_list = [0, 1]  # เริ่มต้นลิสต์ Fibonacci

# คำนวณ Factorial และ Fibonacci
for i in range(1, n+1):
    result *= i
    factorial_list.append(result)  # เพิ่ม Factorial
    if i > 1:
        fibonacci_list.append(fibonacci_list[-1] + fibonacci_list[-2])  # เพิ่ม Fibonacci

# แสดงผล
print(f"Factorial series: {factorial_list}")
print(f"Fibonacci series: {fibonacci_list[:n]}\n")
