# โปรแกรมที่รับขนาดของเมทริกซ์จากผู้ใช้และสร้างเมทริกซ์ขนาดนั้น ๆ โดยใช้เลขสุ่มจาก 0 ถึง 9 และตรวจสอบว่าเมทริกซ์ที่สร้างขึ้นนั้นเป็นเมทริกซ์สมมาตรหรือไม่
import random

print("=" * 80)
size = int(input("Enter the size of the square matrix: "))

if size > 3:
    print("!!! Error: Maximum supported size is 3x3 !!!\n")
else:
    matrix = [[random.randint(0, 9) for _ in range(size)] for _ in range(size)]
    print(f"Matrix: {matrix}")

    is_symmetric = all(matrix[i][j] == matrix[j][i] for i in range(size) for j in range(size))
    print("Matrix is symmetric." if is_symmetric else "Matrix is not symmetric.")
    print("=" * 80 + "\n")