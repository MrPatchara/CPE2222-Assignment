#โปรแกรมสร้างกราฟกระจายเพื่อแสดงความสัมพันธ์ระหว่างข้อมูล 2 ชุด
import matplotlib.pyplot as plt

def plot_scatter(x, y):
    plt.scatter(x, y, c='blue', alpha=0.7)
    plt.title("กราฟกระจาย")
    plt.xlabel("แกน X")
    plt.ylabel("แกน Y")
    plt.grid(True)
    plt.show()

# ตัวอย่างการใช้งาน
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
plot_scatter(x, y)