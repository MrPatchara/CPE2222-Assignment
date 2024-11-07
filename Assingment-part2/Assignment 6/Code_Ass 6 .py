import numpy as np

# ฟังก์ชันอ่านข้อมูลจาก CSV โดยแยกข้อมูลด้วยช่องว่าง (space-separated)
def load_custom_csv(file_name):
    with open(file_name, 'r') as f:
        data = []
        for line in f:
            row = [float(num) for num in line.strip().split()]
            data.append(row)
        return np.array(data)

# โหลดข้อมูลจากไฟล์ CSV และสร้าง 3D matrix D ขนาด (5, 100, 100)
file_names = ['1.csv', '2.csv', '3.csv', '4.csv', '5.csv']
D = np.array([load_custom_csv(file) for file in file_names])

# คำนวณ X เป็นค่าเฉลี่ยของ D ตามแกนที่ 2
X = np.mean(D, axis=2)

# คำนวณ Y เป็นค่าเบี่ยงเบนมาตรฐานของ D ตามแกนที่ 0
Y = np.std(D, axis=0).mean(axis=1, keepdims=True)

# คำนวณ A เป็นผลรวมของ D ตามแกนที่ 1 และ 2
A = np.sum(D, axis=(1, 2)).reshape(1, 5)

# ตรวจสอบขนาดของ X, Y และ A ว่าตรงตามที่กำหนด
print("X shape:", X.shape)  # ควรเป็น (5, 100)
print("Y shape:", Y.shape)  # ควรเป็น (100, 1)
print("A shape:", A.shape)  # ควรเป็น (1, 5)

# จำนวนข้อมูลทั้งหมดใน X
m = X.size

# คำนวณค่า J ตามสูตร
J = (1 / (2 * m)) * np.sum((A @ X - Y.T)**2)

# คำนวณค่า K ตามสูตร
K = (1 / m) * (np.sum((A @ X)**2) - np.sum(Y.T * X))

# แสดงผลลัพธ์
print("X[0,:] =", X[0, :])
print("X[-1,:] =", X[-1, :])
print("Y[0,0] =", Y[0, 0])
print("Y[-1,0] =", Y[-1, 0])
print("A =", A)
print("J =", J)
print("K =", K)
