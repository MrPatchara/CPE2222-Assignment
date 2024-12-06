#โปรแกรมสร้างฮิสโตแกรมจากชุดข้อมูลที่ป้อน
import matplotlib.pyplot as plt

def plot_histogram(data, bins):
    plt.hist(data, bins=bins, edgecolor='black', alpha=0.7)
    plt.title("ฮิสโตแกรมแสดงการกระจายข้อมูล")
    plt.xlabel("ช่วงข้อมูล")
    plt.ylabel("ความถี่")
    plt.show()

# ตัวอย่างการใช้งาน
data = [12, 15, 12, 13, 19, 21, 24, 25, 23, 22, 18, 19, 24, 25, 25, 30, 31, 35]
bins = 5
plot_histogram(data, bins)