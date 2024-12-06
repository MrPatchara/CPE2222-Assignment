# โปรแกรมนี้เป็นตัวอย่างการคำนวณ Eigenvalues และ Eigenvectors ของเมทริกซ์ 2x2
# แก้ไขการเพิ่มการ import ไลบรารี numpy
import numpy as np  # เพิ่มการนำเข้าไลบรารี numpy

print('*' * 70)
print('Eigenvalues and Eigenvectors'.center(70))
print('*' * 70)

A = np.array([[4, 2], [1, 3]])  # เมทริกซ์ 2x2 ตัวอย่าง

# คำนวณ Eigenvalues และ Eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

print("Matrix A:")
print(A)

print("\nEigenvalues:")
print(eigenvalues)

print("\nEigenvectors:")
print(eigenvectors)
