#1.ลำดับจำนวนเต็ม (Integer Sequence) มี นิยามได้ดังนี้ 𝐾𝑛=𝐾𝑛−3+2𝐾𝑛−2+4𝐾𝑛−1 โดยที่ 𝐾2=3,𝐾1=2,𝐾0=1

def calculate_kn(n):
    """คำนวณค่าของ K_n โดยใช้การเวียนซ้ำ"""
    if n == 0:
        return 1
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        return calculate_kn(n - 3) + 2 * calculate_kn(n - 2) + 4 * calculate_kn(n - 1)

def generate_sequence(n):
    """สร้าง Tuple ของลำดับ K_n ตั้งแต่ K0 ถึง Kn"""
    if n < 0:
        raise ValueError("ค่า n ต้องเป็นจำนวนเต็มที่มากกว่าหรือเท่ากับ 0")
    return tuple(calculate_kn(i) for i in range(n + 1))

# รับค่าจากผู้ใช้
try:
    n = int(input("Enter 'n' of Integer Sequence: "))
    result = generate_sequence(n)
    print(f"A tuple of Integer Sequence [n={n}] is {result}\n")
except ValueError as e:
    print("Error:", e)
