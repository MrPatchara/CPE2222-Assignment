import random

# สร้างลิสต์ Factorial โดย n ถูกสุ่มจากช่วงตัวเลขที่กำหนด
print('Generating Randomized Factorial series')
lower = int(input("Enter lower bound for random n: "))
upper = int(input("Enter upper bound for random n: "))
n = random.randint(lower, upper)  # สุ่มค่า n
print(f"Randomly chosen n: {n}")

result = 1
factorial_list = []

for i in range(1, n+1):
    result *= i
    factorial_list.append(result)

# แสดงผล
print(f"Factorial series for random n={n}: {factorial_list}\n")
