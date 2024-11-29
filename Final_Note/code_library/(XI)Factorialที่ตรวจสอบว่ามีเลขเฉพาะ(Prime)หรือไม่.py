# ตรวจสอบว่า Factorial มีค่าเป็นจำนวนเฉพาะหรือไม่
print('Checking if Factorials contain any prime numbers')
n = int(input("Enter 'n' for Factorial series: "))
result = 1
factorial_list = []
prime_check = []

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# คำนวณ Factorial และเช็ค prime
for i in range(1, n+1):
    result *= i
    factorial_list.append(result)
    prime_check.append(is_prime(result))  # เพิ่ม True/False ตามค่าที่เช็ค prime

# แสดงผล
print(f"Factorial series: {factorial_list}")
print(f"Prime check for each Factorial: {prime_check}\n")
