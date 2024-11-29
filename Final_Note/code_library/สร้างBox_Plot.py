#โปรแกรมสร้าง Box Plot เพื่อแสดงการกระจายของข้อมูล
import matplotlib.pyplot as plt

def plot_box(data):
    plt.boxplot(data, patch_artist=True)
    plt.title("Box Plot แสดงการกระจายของข้อมูล")
    plt.xlabel("หมวดหมู่")
    plt.ylabel("ค่า")
    plt.show()

# ตัวอย่างการใช้งาน
data = [7, 8, 9, 10, 15, 16, 22, 24, 27, 28]
plot_box(data)