# แปลง Factorial เป็นเลขฐาน 2, 8, 16
print('Converting Factorials to different bases')
n = int(input("Enter 'n' for Factorial series: "))
result = 1
factorial_list = []

# คำนวณ Factorial และแปลง
for i in range(1, n+1):
    result *= i
    factorial_list.append((result, bin(result), oct(result), hex(result)))  # Factorial, ฐาน 2, 8, 16

# แสดงผล
for i, values in enumerate(factorial_list, start=1):
    print(f"{i}! = {values[0]} | Binary: {values[1]} | Octal: {values[2]} | Hex: {values[3]}")
