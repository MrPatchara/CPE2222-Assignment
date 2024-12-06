#โปรแกรมคำนวณลำดับ Fibonacci สำหรับจำนวน n ที่ผู้ใช้ป้อน
def fibonacci(n):
    if n <= 0:
        return []
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

# รับค่าจากผู้ใช้
n = int(input("ใส่จำนวนตัวเลขในลำดับ Fibonacci: "))
result = fibonacci(n)
print(f"ลำดับ Fibonacci {n} ตัวแรกคือ: {result}")
