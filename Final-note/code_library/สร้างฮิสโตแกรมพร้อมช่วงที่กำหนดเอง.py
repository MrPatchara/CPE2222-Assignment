#โปรแกรมสร้างฮิสโตแกรมที่สามารถกำหนดช่วงของข้อมูลได้เอง
import matplotlib.pyplot as plt

def plot_histogram_with_bins(data, bins):
    plt.hist(data, bins=bins, edgecolor='black', alpha=0.7)
    plt.title("ฮิสโตแกรมพร้อมช่วงที่กำหนดเอง")
    plt.xlabel("ช่วงข้อมูล")
    plt.ylabel("ความถี่")
    plt.show()

# ตัวอย่างการใช้งาน
data = [12, 15, 12, 13, 19, 21, 24, 25, 23, 22, 18, 19, 24, 25, 25, 30, 31, 35]
bins = [10, 15, 20, 25, 30, 35]
plot_histogram_with_bins(data, bins)