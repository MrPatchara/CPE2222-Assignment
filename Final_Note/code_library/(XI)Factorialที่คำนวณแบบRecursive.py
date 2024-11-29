# คำนวณ Factorial แบบ Recursive และเก็บผลลัพธ์ในลิสต์
print('Calculating Factorial series using recursion')
n = int(input("Enter 'n' for Recursive Factorial: "))
factorial_list = []

# ฟังก์ชันคำนวณ Factorial แบบ Recursive
def recursive_factorial(num):
    if num == 1:
        return 1
    return num * recursive_factorial(num - 1)

# สร้างลิสต์ Factorial
for i in range(1, n+1):
    factorial_list.append(recursive_factorial(i))

# แสดงผล
print(f"Factorial series using recursion: {factorial_list}\n")
