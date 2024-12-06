#โปรแกรมสร้างกราฟแท่งและกราฟเส้นในกราฟเดียวเพื่อเปรียบเทียบข้อมูล
import matplotlib.pyplot as plt

def plot_bar_and_line(categories, bar_values, line_values, bar_label, line_label):
    fig, ax1 = plt.subplots()

    # กราฟแท่ง
    ax1.bar(categories, bar_values, color='b', alpha=0.6, label=bar_label)
    ax1.set_xlabel('หมวดหมู่')
    ax1.set_ylabel('ค่ากราฟแท่ง', color='b')

    # กราฟเส้น
    ax2 = ax1.twinx()
    ax2.plot(categories, line_values, color='r', marker='o', label=line_label)
    ax2.set_ylabel('ค่ากราฟเส้น', color='r')

    # แสดงกราฟ
    fig.tight_layout()
    plt.title("กราฟแท่งและกราฟเส้นในกราฟเดียว")
    plt.show()

# ตัวอย่างการใช้งาน
categories = ["หมวด A", "หมวด B", "หมวด C", "หมวด D"]
bar_values = [20, 35, 30, 35]
line_values = [25, 32, 34, 20]
plot_bar_and_line(categories, bar_values, line_values, "ยอดขาย", "กำไร")