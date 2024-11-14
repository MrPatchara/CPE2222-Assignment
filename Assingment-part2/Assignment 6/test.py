import numpy as np

# สร้างอาร์เรย์ 3 มิติสำหรับเก็บข้อมูลจากไฟล์ CSV
D = np.zeros((5, 100, 100))

# โหลดไฟล์ CSV แต่ละไฟล์เข้าไปในอาร์เรย์ 3 มิติ
for i in range(1, 6):
    try:
        # พยายามโหลดไฟล์ด้วย delimiter เป็นคอมมา
        D[i-1] = np.loadtxt(f"{i}.csv", delimiter=",")
    except ValueError:
        # หากเกิดข้อผิดพลาด พยายามโหลดด้วย delimiter เป็นช่องว่าง
        try:
            D[i-1] = np.loadtxt(f"{i}.csv", delimiter=" ")
        except ValueError as e:
            print(f"Error loading file {i}.csv: {e}")
            break

# คำนวณค่าเฉลี่ยของ D ในแกนที่ 0 เพื่อให้ได้ mean_D ขนาด (100, 100)
mean_D = np.mean(D, axis=0)

# ยุบข้อมูลจาก (100, 100) เป็น (100, 5) โดยการคำนวณค่าเฉลี่ยทุกๆ 20 ค่าในแนวนอน
x = np.mean(mean_D.reshape(100, 5, 20), axis=2)

# คำนวณค่าเบี่ยงเบนมาตรฐานของ D เพื่อให้ได้ std_D ขนาด (100, 100)
std_D = np.std(D, axis=0)

# คำนวณค่าเฉลี่ยของค่าเบี่ยงเบนมาตรฐาน std_D เพื่อให้ได้ y ขนาด (100,1)
y = np.mean(std_D, axis=0).reshape(100, 1)

# คำนวณ A เป็นผลรวมของ D ตามแกนที่ 1 และ 2
a = np.sum(D, axis=(1, 2)).reshape(1, 5)

# ตรวจสอบขนาดของ X, Y และ A ว่าตรงตามที่กำหนด
print("#" * 80)
print(" ตรวจสอบขนาดของ X, Y, A และ D ว่าตรงตามที่กำหนด")
print("-" * 80)
print("X shape:", x.shape)  # ควรเป็น (5, 100)
print("Y shape:", y.shape)  # ควรเป็น (100, 1)
print("A shape:", a.shape)  # ควรเป็น (1, 5)
print("D shape:", D.shape)  # ควรเป็น (5, 100, 100)

# คํานวณค่า J ตามสูตร
m = x.size
J = (1 / (2 * m)) * np.sum((np.dot(a, x.T) - y) ** 2)

# คำนวณค่า K ตามสูตรและแสดงผลค่า K เป็น (1, 5)
K = (1 / m) * (np.sum(np.dot(a, x.T) ** 2, axis=1) - np.sum(y * x, axis=0)).reshape(1, 5)


# แสดงผลลัพธ์ พร้อมขึ้นบรรทัดใหม่
print("-" * 80)
print("x[0,:] =", x[0, :])
print("x[-1,:] =", x[-1, :], "\n")

print("y[0,0] =", y[0, 0])
print("y[-1,0] =", y[-1, 0], "\n")

print("A =", a, "\n")

print("J =", J, "\n")
print("K =", K)