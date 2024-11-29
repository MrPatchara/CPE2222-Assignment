# คำนวณ Factorial แบบเรียงลำดับจาก n ลงมาถึง 1
print('Generating Reverse Factorial series')
n = int(input("Enter 'n' for Reverse Factorial series: "))
result = 1
reverse_factorial_list = []

# คำนวณ Factorial ทั้งหมดก่อนแล้วค่อยย้อนกลับ
for i in range(1, n+1):
    result *= i

# Loop ย้อนกลับ
for i in range(n, 0, -1):
    reverse_factorial_list.append(result)
    result //= i  # หารกลับเพื่อลด Factorial

# แสดงผล
print(f"Reverse Factorial series: {reverse_factorial_list}\n")
