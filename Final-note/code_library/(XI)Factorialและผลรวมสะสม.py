# คำนวณ Factorial และหาผลรวมสะสมของ Factorial
print('Generating Factorial series with cumulative sums')
n = int(input("Enter 'n' for Factorial series: "))
result = 1
factorial_list = []
cumulative_sum = 0
cumulative_sum_list = []

# Loop คำนวณ
for i in range(1, n+1):
    result *= i
    factorial_list.append(result)  # เพิ่มค่า factorial ในลิสต์
    cumulative_sum += result  # สะสมผลรวม
    cumulative_sum_list.append(cumulative_sum)

# แสดงผล
print(f"Factorial series: {factorial_list}")
print(f"Cumulative sum of factorials: {cumulative_sum_list}\n")
