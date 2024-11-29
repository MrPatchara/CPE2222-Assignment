#โปรแกรมสร้างกราฟเส้นเปรียบเทียบข้อมูลสองชุด
import matplotlib.pyplot as plt

def plot_comparison(x, y1, y2, labels):
    plt.plot(x, y1, label=labels[0], marker='o')
    plt.plot(x, y2, label=labels[1], marker='s')
    plt.title("กราฟเปรียบเทียบข้อมูลสองชุด")
    plt.xlabel("แกน X")
    plt.ylabel("แกน Y")
    plt.legend()
    plt.grid(True)
    plt.show()

# ตัวอย่างการใช้งาน
x = [1, 2, 3, 4, 5]
y1 = [10, 20, 30, 40, 50]
y2 = [15, 25, 35, 45, 55]
labels = ["ข้อมูลชุดที่ 1", "ข้อมูลชุดที่ 2"]
plot_comparison(x, y1, y2, labels)